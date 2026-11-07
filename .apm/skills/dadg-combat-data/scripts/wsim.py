# Port of TaleWorlds.Core Crafting.CraftedItemGenerationHelper stats (1.4.8).
# Usage: wsim.py <out.csv> pieces=<xml> templates=<xml> descs=<xml> items=<xml> ...
import sys, csv, re, math
import xml.etree.ElementTree as ET

MELEE, NO1H, WIDE = 'MeleeWeapon', 'NotUsableWithOneHand', 'WideGrip'
PT = dict(Blade=0, Guard=1, Handle=2, Pommel=3)
out = sys.argv[1]
src = {}
for a in sys.argv[2:]:
    k, v = a.split('=', 1)
    src.setdefault(k, []).append(v)


def f(n, k, d=0.):
    v = n.get(k)
    return float(v) if v not in (None, '') else d


class P: pass


pieces = {}
for fn in src['pieces']:
    for n in ET.parse(fn).getroot().iter('CraftingPiece'):
        p = P()
        p.id = n.get('id')
        p.type = PT[n.get('piece_type')]
        p.w = f(n, 'weight')
        if n.get('length') is not None:
            p.L = .01 * float(n.get('length'))
            p.dn = p.dp = p.L / 2
        else:
            p.dn = .01 * f(n, 'distance_to_next_piece')
            p.dp = .01 * f(n, 'distance_to_previous_piece')
            p.L = p.dn + p.dp
        p.I = p.w * p.L * p.L / 12
        p.com = p.L * f(n, 'center_of_mass', .5)
        p.tier = int(f(n, 'tier', 1))
        fs = n.get('full_scale')
        p.full = (fs == 'true') if fs is not None else p.type in (1, 3)
        b = n.find('BuildData')
        p.off = .01 * f(b, 'piece_offset') if b is not None else 0
        p.poff = .01 * f(b, 'previous_piece_offset') if b is not None else 0
        p.noff = .01 * f(b, 'next_piece_offset') if b is not None else 0
        bd = n.find('BladeData')
        p.tf = p.sf = 0
        p.tt = p.st = ''
        p.stack = 1
        if bd is not None:
            p.stack = int(f(bd, 'stack_amount', 1))
            t = bd.find('Thrust')
            s = bd.find('Swing')
            if t is not None:
                p.tf, p.tt = float(t.get('damage_factor')), t.get('damage_type')
            if s is not None:
                p.sf, p.st = float(s.get('damage_factor')), s.get('damage_type')
        pieces[p.id] = p

templates = {}
for fn in src['templates']:
    for n in ET.parse(fn).getroot().iter('CraftingTemplate'):
        t = P()
        t.bo = [(PT[d.get('piece_type')], int(d.get('build_order'))) for d in n.find('PieceDatas')]
        t.desc = [d.get('id') for d in n.find('WeaponDescriptions')]
        templates[n.get('id')] = t

descs = {}
for fn in src['descs']:
    for n in ET.parse(fn).getroot().iter('WeaponDescription'):
        d = P()
        d.cls = n.get('weapon_class')
        d.flags = {x.get('value') for x in n.iter('WeaponFlag')}
        d.avail = {x.get('id') for x in n.iter('AvailablePiece')}
        descs[n.get('id')] = d


def strike(sw, ip, w, L, I, com):
    n = L * ip - com
    n2 = sw * (.5 + com)
    n5 = .5 * w * n2 * n2 + .5 * I * sw * sw
    n6 = (n2 + sw * n) / (1 / w + n * n / I)
    n7 = n2 - n6 / w
    n8 = sw - n6 * n / I
    return .067 * (n5 - (.5 * w * n7 * n7 + .5 * I * n8 * n8) + .5)


def baseblow(sw, L, w, I, com, ip):
    ip = min(ip, .93)
    x = min(max(.4 / L, 0), 1)
    best = 0
    for i in range(5):
        q = ip + i / 4 * x
        if q >= 1:
            break
        best = max(best, strike(sw, q, w, L, I, com))
    return best


def layer(span, power, maxT, inertia, drag):
    a, v, t = 0, .01, 0
    while a < span:
        tq = min(power / v, maxT) - v * drag
        v += .009999999776482582 * tq / inertia
        a += v * .009999999776482582
        t += .009999999776482582
    return t


def tlayer(dist, power, maxF, mass):
    a, v, t = 0, .01, 0
    while a < dist:
        fc = min(power / v, maxF)
        v += .01 * fc / mass
        a += v * .01
        t += .01
    return t


def design(tp, used):
    """used: {type:(piece,scale)}"""
    S = lambda i: used[i][1]
    D = {}
    n, n2 = 0., 0.
    piv = {}
    for ty, o in tp.bo:
        if ty not in used:
            continue
        p, s = used[ty]
        g = (o > 0) - (o < 0)
        if g == 0:
            n2 += p.off * s
            n -= p.off * s
        elif g < 0:
            n += p.dn * s + p.off * s - p.noff * s
        else:
            n2 += p.dp * s + p.off * s - p.poff * s
        piv[ty] = g * (n if g < 0 else n2) + (p.off * s if g == 0 else 0)
        if g == 0:
            n += (p.dp - p.poff) * s
            n2 += (p.dn - p.noff) * s
        elif g < 0:
            n += (p.dp - p.poff) * s
        else:
            n2 += (p.dn - p.noff) * s
    bl, bs = used[0]
    a = piv[0] + bl.dn * bs
    m = 0
    for ty in sorted(used):
        p, s = used[ty]
        if p.dn * s > m:
            m = p.dn * s + p.off * s
    return max(a, m)


def stats(tp, d, used):
    fl = d.flags
    swn = lambda p, s: p.w * (s ** 3 if p.full else s) if s != 1 else p.w
    W = round(sum(swn(p, s) for p, s in used.values()), 2)
    R = round(design(tp, used), 2)
    # centre of mass
    num, top, bot = 0., 0., 0.
    for ty, o in tp.bo:
        if ty not in used:
            continue
        p, s = used[ty]
        w, L, c = swn(p, s), p.L * s, p.com * s
        if o < 0:
            num -= (bot + (L - c)) * w
            bot += L
        else:
            num += (top + c) * w
            top += L
    hp, hs = used[2]
    com = num / W - (hp.dp * hs - hp.off * hs)
    # inertia (note: the engine walks build order; pommel lands after the blade)
    x = -com
    I = 0.
    for ty, o in tp.bo:
        if ty not in used:
            continue
        p, s = used[ty]
        off = x + p.com
        I += p.I + swn(p, s) * off * off
        x += p.L * s
    Ish = I + W * (.5 + com) ** 2
    Igr = I + W * com * com
    # swing speed
    q = Ish + .9
    n2, n3, n4, n5, n6 = 170., 90., 27., 15., 7.
    twoh = MELEE in fl and NO1H in fl
    wg = WIDE in fl
    if twoh:
        if wg:
            q += 1.5; n6 *= 4; n5 *= 1.7; n3 *= 1.3; n2 *= 1.15
        else:
            q += 1; n6 *= 2.4; n5 *= 1.3; n3 *= 1.35; n2 *= 1.15
    n4 = max(1, n4 - q); n5 = max(1, n5 - q); n6 = max(1, n6 - q)
    drag = 3.9 * R * (1 if (MELEE in fl and wg) else .3)
    t = layer(1.5, 200, n4, 2 + q, drag) + layer(1.5, n2, n5, 1 + q, drag) + layer(1.5, n3, n6, .5 + q, drag)
    sw = 20.8 / (.33 * t)
    # thrust speed
    q = 1.8 + W + Igr * .2
    a2, a3, a4, a5 = 170., 90., 24., 15.
    if twoh and not wg:
        q += .6; a5 *= 1.9; a4 *= 1.1; a3 *= 1.2; a2 *= 1.05
    elif twoh and wg:
        q += .9; a5 *= 2.1; a4 *= 1.2; a3 *= 1.2; a2 *= 1.05
    t = tlayer(.6, 250, 48, 4 + q) + tlayer(.6, a2, a4, 2 + q) + tlayer(.6, a3, a5, .5 + q)
    th = 3.85 / (.33 * t)
    # handling
    g = Igr
    if twoh:
        g = g * .5 + .9
    elif MELEE in fl and wg:
        g = g * .4 + 1
    else:
        g += .7
    hand = round(100 * (1 / g) ** .55)
    # damage
    best = 0
    ip = .93
    while ip > .5:
        best = max(best, baseblow(sw, R, W, I, com, ip))
        ip -= .05
    b = used[0][0]
    swd = best * b.sf
    thd = .125 * (.5 * (W + 2.5) * th * th) * b.tf
    if d.cls == 'Javelin':
        thd = .125 * (.5 * W * th * th) * b.tf * 9
        swd = 0
    tier = int(sum(p.tier for p, s in used.values()) / len(used))
    return dict(W=W, R=round(R * 100), ss=math.floor(sw * 4.5454545), ts=math.floor(th * 11.764706), hand=hand,
                swd=round(swd), thd=round(thd), st=b.st, tt=b.tt, sf=b.sf, tf=b.tf, tier=tier, bl=b.id, stack=b.stack)


rows = []
for fn in src['items']:
    txt = open(fn, encoding='utf-8-sig').read()
    root = ET.fromstring(txt)
    for it in root.iter('CraftedItem'):
        tn = it.get('crafting_template')
        tp = templates.get(tn)
        if tp is None:
            print('NO TEMPLATE', it.get('id'), tn)
            continue
        used = {}
        miss = []
        for pc in it.iter('Piece'):
            p = pieces.get(pc.get('id'))
            if p is None:
                miss.append(pc.get('id'))
                continue
            used[p.type] = (p, f(pc, 'scale_factor', 100) / 100)
        if miss or 0 not in used or 2 not in used:
            print('MISSING', it.get('id'), miss)
            continue
        ids = {p.id for p, s in used.values()}
        usage = [dn for dn in tp.desc if dn in descs and ids <= descs[dn].avail] or tp.desc[:1]
        for i, dn in enumerate(usage):
            r = stats(tp, descs[dn], used)
            r.update(id=it.get('id'), name=re.sub(r'^\{=[^}]*\}', '', it.get('name', '')), tmpl=tn, usage=dn, alt=i, merch=it.get('is_merchandise'), scales=' '.join(str(int(s * 100)) for t, (p, s) in sorted(used.items())))
            rows.append(r)

with open(out, 'w', newline='', encoding='utf8') as fh:
    w = csv.DictWriter(fh, ['id', 'name', 'tmpl', 'usage', 'alt', 'W', 'R', 'ss', 'ts', 'hand', 'swd', 'st', 'thd', 'tt', 'sf', 'tf', 'tier', 'bl', 'stack', 'scales', 'merch'])
    w.writeheader()
    w.writerows(rows)
print(len(rows), 'rows')
