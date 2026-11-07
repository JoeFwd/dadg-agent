# Applies the T1-T6 weapon ladder and the armour material table to the DADG content module.
#
# Usage: python apply_combat_data.py <DellarteDellaGuerra module> <Native module>
#
# Damage is never set by hand: piece weights and damage types are applied first, then wsim.py gives
# the stats of each weapon and damage_factor is solved from the target. Safe to run again. Ends with
# a validator, because one bad node in the merged XML drops every object loaded after it.
import csv
import os
import re
import statistics
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

MODULE, NATIVE = sys.argv[1:3]
ITEMS = MODULE + '/ModuleData/items'
PIECES = ITEMS + '/DDG_CraftingPieces.xml'
TEMPLATES = ITEMS + '/dadg_crafting_templates.xml'
DESCRIPTIONS = ITEMS + '/dadg_weapon_descriptions.xml'
WEAPONS = ITEMS + '/DDG_Weapons.xml'
ARMOURS = ITEMS + '/items.xml'
FIREARMS = MODULE + '/ModuleData/Firearm/firearm_items.xml'
TABLE = MODULE + '/ModuleData/CustomXml/dadg_combat_items.xml'
WSIM = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wsim.py')

# family -> (swing T1..T6, thrust T1..T6); 0 = keep the current factor
LADDER = {
    'sword1h': ([48, 56, 64, 70, 76, 82], [26, 30, 34, 38, 42, 46]),
    'longsword': ([0, 0, 68, 74, 80, 86], [0, 0, 38, 42, 46, 50]),
    'sword2h': ([0, 0, 92, 102, 112, 122], [0, 0, 42, 46, 50, 54]),
    'axe1h': ([44, 58, 68, 76, 82, 88], [0] * 6),
    'mace': ([26, 36, 46, 54, 62, 68], [0] * 6),
    'staff': ([44, 54, 64, 0, 0, 0], [20, 24, 28, 0, 0, 0]),
    'polehammer': ([0, 0, 0, 72, 80, 88], [0, 0, 0, 38, 42, 46]),
    'pollaxe': ([0, 0, 105, 118, 130, 142], [0, 0, 30, 34, 38, 42]),
    'tool2h': ([50, 0, 0, 0, 0, 0], [24, 0, 0, 0, 0, 0]),
    'bill': ([64, 76, 88, 100, 112, 124], [24, 28, 32, 36, 40, 44]),
    'spear': ([0] * 6, [24, 28, 32, 36, 40, 44]),
    'lance': ([0] * 6, [0, 0, 0, 42, 46, 50]),
    'pike': ([0] * 6, [0, 30, 34, 38, 42, 46]),
    'javelin': ([0] * 6, [0, 60, 78, 96, 110, 124]),
}

WEAPON_TIERS = {
    'short_messer': ('sword1h', 1), 'griffin_messer': ('sword1h', 2), 'baselard': ('sword1h', 2),
    'wakefield_hanger': ('sword1h', 3), 'hanger': ('sword1h', 3), 'falstaff': ('sword1h', 3),
    'kleinbusch': ('sword1h', 3), 'scottish_arming_sword': ('sword1h', 4), 'wallace_A462': ('sword1h', 4),
    'glasgow_castillon': ('sword1h', 5), 'castillon_b': ('sword1h', 5), 'castillon_falchion': ('sword1h', 6),
    'Ely_XV_3': ('longsword', 3), 'wallace_A465': ('longsword', 4), 'coventry2': ('longsword', 5),
    'castillon_c': ('longsword', 6),
    'type_xxa': ('sword2h', 3), 'castillon_b_twohander': ('sword2h', 4), 'IX_633_twohander': ('sword2h', 4),
    'stcatherine': ('sword2h', 5), 'gaelic_fancy_longsword': ('sword2h', 6),
    'dadg_peasant_sickle_1_t1': ('axe1h', 1), 'dadg_peasant_hatchet_1_t1': ('axe1h', 1),
    'dadg_peasant_pickaxe_1_t1': ('axe1h', 2), 'rigsby_axe': ('axe1h', 3),
    'dadg_peasant_hammer_1_t1': ('mace', 1), 'ddg_mace_oldthamesmace': ('mace', 2),
    'ddg_mace_basicmace': ('mace', 3), 'ddg_mace_frenchmace': ('mace', 4),
    'ddg_mace_writhenmace': ('mace', 5), 'ddg_mace_horsemanshammer': ('mace', 6),
    'dadg_peasant_2haxe_1_t1': ('tool2h', 1), 'dadg_peasant_polearm_1_t1': ('tool2h', 1),
    'dadg_peasant_pitchfork_2_t1': ('tool2h', 1), 'dadg_peasant_pitchfork_1_t1': ('tool2h', 1),
    'ddg_quarterstaff': ('staff', 1), 'ddg_brogitstaff': ('staff', 2), 'ddg_warclub': ('staff', 3),
    'ddg_leadhammer': ('polehammer', 4), 'ddg_pollhammer': ('polehammer', 5),
    'ddg_irishaxe': ('pollaxe', 3), 'ddg_lochaberaxe': ('pollaxe', 4), 'execution_axe': ('pollaxe', 4),
    'ddg_poleaxe_poleaxea': ('pollaxe', 5), 'ddg_poleaxe_poleaxeb': ('pollaxe', 6),
    'ddg_voulge': ('bill', 2), 'ddg_winchester_glaive': ('bill', 3), 'ddg_polearm_italy_billhook': ('bill', 3),
    'ddg_jedbugh_staff': ('bill', 3), 'ddg_polearm_billhook': ('bill', 4),
    'ddg_polearm_welsh_billhook': ('bill', 4), 'ddg_polearm_halberda': ('bill', 4),
    'ddg_polearm_halberdb': ('bill', 5),
    'ddg_polearm_boarspear': ('spear', 2), 'ddg_polearm_longspear': ('spear', 3), 'ddg_partisan': ('spear', 4),
    'lance_b': ('lance', 4), 'lance_a_red': ('lance', 4), 'lance_a_black': ('lance', 4),
    'ddg_pike_halfpike': ('pike', 2), 'ddg_pike_german': ('pike', 3), 'ddg_pike_flemish': ('pike', 4),
    'ddg_polearm_longpike': ('pike', 5),
    'ddg_javelin': ('javelin', 2), 'ddg_javelin3': ('javelin', 3), 'ddg_javelin2': ('javelin', 4),
}

# items that take their tier from the table without being re-statted
EXTRA_TIERS = {
    'battania_mace_1_t2': 2, 'short_sword_t3': 2,  # XSLT copies of ddg_mace_oldthamesmace and baselard
    'yew_longbow_weak': 2, 'yew_longbow': 3, 'yew_longbow_strong': 5,
    'ddg_crossbow_g': 2, 'dadg_crossbow': 3, 'dadg_arbalest': 4, 'ddg_crossbow_d': 5,
    'handgonne': 3, 'english_arquebus_1': 4, 'lgarquebus_bronze': 5,
    'bucklers_a': 2, 'bucklers_b': 2, 'bucklers_c': 2,
    'shield_big': 4, 'burgundian_shield': 5, 'burgundian_shield_a': 4, 'burgundian_shield_b': 4,
}

RANGED_DAMAGE = {
    'yew_longbow_weak': 38, 'yew_longbow': 46, 'yew_longbow_strong': 62,
    'ddg_crossbow_g': 75, 'ddg_crossbow_d': 96,
}
FIREARM_DAMAGE = {'handgonne': 90, 'english_arquebus_1': 105, 'lgarquebus_bronze': 120}
PRICES = {'bundle_of_arrows': 100, 'linen_quiver': 150}
# these carried value="70000", which beat any tier
UNPRICED = ['shield_big', 'burgundian_shield', 'burgundian_shield_a', 'burgundian_shield_b']

# piece -> weight; DADG's bills weighed 0.8 and its pikes 1.0 against vanilla's 1.9 and 2.2, these
# stop short of vanilla because the weapons are longer and swing speed drops fast
PIECE_WEIGHTS = {
    'ddg_england_twohandedpolearm_halbertahaft': 1.2, 'ddg_england_twohandedpolearm_halbertbhaft': 1.2,
    'ddg_england_twohandedpolearm_halbertbhead': 0.5, 'ddg_england_winchester_glaive_head': 0.5,
    'ddg_england_voulge_head': 0.45, 'ddg_england_twohandedpolearm_voulge_haft': 1.3,
    'ddg_england_twohandedpolearm_billhook': 0.55, 'ddg_italy_twohandedpolearm_billhook': 0.55,
    'ddg_wales_twohandedpolearm_billhook': 0.55,
    'ddg_jedbugh_staff_head': 0.6, 'ddg_jedbugh_staff_shaft': 1.1,
    'ddg_england_twohandedpolearm_longspearhaft': 0.9, 'ddg_england_twohandedpolearm_boarspearhead': 0.5,
    'ddg_england_pike_halfpikehaft': 1.4, 'ddg_england_pike_haft': 1.6,
    'ddg_england_twohandedpolearm_longpikehaft': 1.0,
    'lance_a_red': 1.07, 'lance_a_black': 1.07, 'lance_b': 1.07,
}

SWING_TYPES = {
    'ddg_quarterstaff_head': 'Blunt', 'ddg_brogit_staff_head': 'Blunt', 'ddg_war_club_head': 'Blunt',
    'ddg_leadhammer_head': 'Blunt', 'ddg_pollhammer_head': 'Blunt',
}
ITEM_SWING_TYPES = {
    'dadg_peasant_sickle_1_t1': 'Cut', 'dadg_peasant_polearm_1_t1': 'Cut', 'dadg_peasant_pickaxe_1_t1': 'Pierce',
}
TOURNEY_ITEMS = ['tourney_sword_one', 'tourney_sword_two', 'tourney_club']

# the spear and the long pike shared one head but need different thrust factors
LONG_SPEAR_HEAD = 'ddg_england_twohandedpolearm_longspearhead'
LONG_PIKE_HEAD = 'ddg_england_twohandedpolearm_longpikehead'
LONG_PIKE = 'ddg_polearm_longpike'
LONG_PIKE_TEMPLATE = '10_Pike'
LONG_PIKE_USAGES = ['dadg_TwoHandedPolearm_Pike', 'dadg_TwoHandedPolearm_Bracing']

# highest arm_armor a sleeve of that material may have
ARM_CAPS = {'Cloth': 8, 'Padded': 14, 'Mail': 26, 'Brigandine': 24, 'Plate': 40}
FALLBACK = {'Cloth': 'Cloth', 'Leather': 'Padded', 'Chainmail': 'Mail', 'Plate': 'Plate'}

# body armour id -> (torso, sleeves); read from the FBX arm faces where they could be read, the
# item name otherwise. Anything not listed keeps its XML material on both, see ../doc.
# one factor by design, the items on them land either side of the target
SHARED_BLADES = {'ddg_lochaber_axe_head', 'lance_head_01'}
# damage is an integer, so re-solving a factor that already lands on target would only add noise
SETTLED = 0.015
BODY_RULES = [
    (r'^(flemish_armor)$', ('Plate', 'Padded')),
    (r'^flemish_armor_a$', ('Plate', 'Mail')),
    (r'^germancuirass', ('Plate', 'Mail')),
    (r'^lubeckjack_germanarmharness$', ('Padded', 'Plate')),
    (r'^lubeckjack_shortmaillesleeves$', ('Padded', 'Mail')),
    (r'^brigandine_over_mail', ('Brigandine', 'Mail')),
    (r'^brigandine_with_coat$', ('Brigandine', 'Padded')),
    (r'^brigandine_(with_pauldrons|with_older_arms|with_plackart|with_bigger_pauldrons)', ('Brigandine', 'Plate')),
    (r'^brigandine_(doublet_pauldrons_|[abc]$)', ('Brigandine', 'Cloth')),
    (r'^breastplate_with_mail$', ('Plate', 'Mail')),
    (r'^breastplate_over_doublet', ('Plate', 'Cloth')),
    (r'^(livery_coat_opened_over_breastplate|livery_coat_with_breastplate|cuirass_with_puffy_sleeves)$', ('Plate', 'Cloth')),
    (r'^livery_coat_opened_over_brigandine$', ('Brigandine', 'Cloth')),
    (r'^(simple_)?livery_coat_opened_over_jack$', ('Padded', 'Cloth')),
    (r'^(simple_)?livery_coat_over_mail$', ('Mail', 'Mail')),
    (r'^jack_with_arm_plates$', ('Padded', 'Plate')),
    (r'^jack_sleeveless_with_mail_sleeves$', ('Padded', 'Mail')),
    (r'^jack_sleeveless_with_splints$', ('Padded', 'Brigandine')),
    (r'^jack_wiith_breastplate$', ('Plate', 'Padded')),
    (r'^(jack_with_livery_and_puffy_sleeves|jack_short_with_livery)$', ('Padded', 'Cloth')),
    (r'^(jack|flemish_jack|jack_with_livery_colors)$', ('Padded', 'Padded')),
    (r'^cotun', ('Padded', 'Padded')),
    (r'^(irish_hauberk|mailshirt_|coustiller_armor)', ('Mail', 'Mail')),
]
LEG_RULES = [(r'maillestrips', 'Mail'), (r'legsplints', 'Brigandine')]


def read(path):
    with open(path, encoding='utf-8', newline='') as fh:
        return fh.read()


def write(path, text):
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)


def piece_span(text, piece):
    start = re.search(r'<CraftingPiece\s+id="%s"' % re.escape(piece), text)
    if not start:
        sys.exit('no piece ' + piece)
    return start.start(), text.index('</CraftingPiece>', start.start()) + len('</CraftingPiece>')


def edit_piece(text, piece, edit):
    a, b = piece_span(text, piece)
    return text[:a] + edit(text[a:b]) + text[b:]


def set_attr(block, tag, attr, value):
    new, n = re.subn(r'(<%s\b[^>]*?\b%s=")[^"]*(")' % (tag, attr), lambda m: m.group(1) + str(value) + m.group(2),
                     block, count=1, flags=re.S)
    if not n:
        sys.exit('no %s %s in %s' % (tag, attr, block[:80]))
    return new


def split_long_pike_head():
    pieces = read(PIECES)
    if LONG_PIKE_HEAD in pieces:
        return
    a, b = piece_span(pieces, LONG_SPEAR_HEAD)
    copy = pieces[a:b].replace('id="%s"' % LONG_SPEAR_HEAD, 'id="%s"' % LONG_PIKE_HEAD).replace('Long Spear Head', 'Long Pike Head')
    write(PIECES, pieces[:b] + '\n\n  ' + copy + pieces[b:])

    weapons = read(WEAPONS)
    a = weapons.index('id="%s"' % LONG_PIKE)
    b = weapons.index('</CraftedItem>', a)
    write(WEAPONS, weapons[:a] + weapons[a:b].replace(LONG_SPEAR_HEAD, LONG_PIKE_HEAD) + weapons[b:])

    templates = read(TEMPLATES)
    a = templates.index('id="%s"' % LONG_PIKE_TEMPLATE)
    line = re.compile(r'([ \t]*)<UsablePiece piece_id="%s" />(\r?\n)' % LONG_SPEAR_HEAD)
    m = line.search(templates, a)
    templates = templates[:m.end()] + '%s<UsablePiece piece_id="%s" />%s' % (m.group(1), LONG_PIKE_HEAD, m.group(2)) + templates[m.end():]
    write(TEMPLATES, templates)

    descriptions = read(DESCRIPTIONS)
    for usage in LONG_PIKE_USAGES:
        a = descriptions.index('id="%s"' % usage)
        line = re.compile(r'([ \t]*)<AvailablePiece id="%s" />(\r?\n)' % LONG_SPEAR_HEAD)
        m = line.search(descriptions, a)
        descriptions = descriptions[:m.end()] + '%s<AvailablePiece id="%s" />%s' % (m.group(1), LONG_PIKE_HEAD, m.group(2)) + descriptions[m.end():]
    write(DESCRIPTIONS, descriptions)


def blade_of_items():
    return {i: [p.get('id') for p in it.iter('Piece')] for it in ET.parse(WEAPONS).getroot().iter('CraftedItem')
            for i in [it.get('id')]}


def simulate():
    with tempfile.TemporaryDirectory() as tmp:
        out = tmp + '/w.csv'
        subprocess.run([sys.executable, '-I', WSIM, out, 'pieces=' + PIECES, 'pieces=' + NATIVE + '/ModuleData/crafting_pieces.xml',
                        'templates=' + TEMPLATES, 'descs=' + DESCRIPTIONS, 'items=' + WEAPONS],
                       check=True, stdout=subprocess.DEVNULL)
        with open(out, encoding='utf8') as fh:
            rows = {}
            for r in csv.DictReader(fh):
                rows.setdefault(r['id'], r)  # first usage is the one the ladder targets
            return rows


def apply_geometry_and_types():
    pieces = read(PIECES)
    for piece, weight in PIECE_WEIGHTS.items():
        pieces = edit_piece(pieces, piece, lambda b: set_attr(b, 'CraftingPiece', 'weight', weight))
    rows = simulate()
    swing = dict(SWING_TYPES)
    swing.update({rows[i]['bl']: t for i, t in ITEM_SWING_TYPES.items()})
    for piece, kind in swing.items():
        pieces = edit_piece(pieces, piece, lambda b: set_attr(b, 'Swing', 'damage_type', kind))
    for item in TOURNEY_ITEMS:
        def blunt(block):
            for tag in ('Thrust', 'Swing'):
                if re.search(r'<%s\b' % tag, block):
                    block = set_attr(block, tag, 'damage_type', 'Blunt')
            return block
        pieces = edit_piece(pieces, rows[item]['bl'], blunt)
    write(PIECES, pieces)


def solve_factors():
    rows = simulate()
    wanted = {}
    for item, (family, tier) in WEAPON_TIERS.items():
        r = rows[item]
        swing, thrust = LADDER[family][0][tier - 1], LADDER[family][1][tier - 1]
        sf, tf, sd, td = float(r['sf']), float(r['tf']), int(r['swd']), int(r['thd'])
        factors = wanted.setdefault(r['bl'], ([], []))
        if swing and sf and sd:
            factors[0].append((swing / sd, sf))
        if thrust and tf and td:
            factors[1].append((thrust / td, tf))
    pieces = read(PIECES)
    for blade, (swing, thrust) in wanted.items():
        def edit(block):
            for tag, solved in (('Swing', swing), ('Thrust', thrust)):
                ratio = statistics.mean(r for r, _ in solved) if solved else 1
                if abs(ratio - 1) > SETTLED:
                    block = set_attr(block, tag, 'damage_factor', round(statistics.mean(r * f for r, f in solved), 2))
            return block
        pieces = edit_piece(pieces, blade, edit)
    write(PIECES, pieces)


def item_block(text, item):
    start = re.search(r'<Item\s+id="%s"' % re.escape(item), text)
    if not start:
        sys.exit('no item ' + item)
    return start.start(), text.index('</Item>', start.start())


def edit_item(text, item, edit):
    a, b = item_block(text, item)
    return text[:a] + edit(text[a:b]) + text[b:]


def set_item_attr(block, attr, value):
    new, n = re.subn(r'\b%s="[^"]*"' % attr, '%s="%s"' % (attr, value), block, count=1)
    if not n:
        sys.exit('no %s in %s' % (attr, block[:80]))
    return new


def drop_item_value(block):
    tag_end = block.index('>')
    return re.sub(r'\s+value="\d+"', '', block[:tag_end]) + block[tag_end:]


def body_materials(item):
    for rule, materials in BODY_RULES:
        if re.search(rule, item.get('id')):
            return materials
    material = FALLBACK.get(item.find('.//Armor').get('material_type'), 'Cloth')
    return material, material


def armour_row(item):
    armour = item.find('.//Armor')
    kind = item.get('Type')
    if armour is None:
        return None
    if kind == 'BodyArmor':
        torso, sleeves = body_materials(item)
        row = {'torso': torso, 'shoulder': sleeves, 'arm': sleeves}
        # skirts and tassets: the body armour's own leg_armor sits on the legs
        if int(armour.get('leg_armor', 0)):
            row['legs'] = torso
        return row
    material = FALLBACK.get(armour.get('material_type'), 'Cloth')
    if kind == 'HeadArmor':
        return {'head': material}
    if kind == 'HandArmor':
        return {'arm': material}
    if kind == 'LegArmor':
        for rule, leg_material in LEG_RULES:
            if re.search(rule, item.get('id')):
                material = leg_material
        return {'legs': material}
    return None


def apply_item_data():
    text = read(ARMOURS)
    for item, damage in RANGED_DAMAGE.items():
        text = edit_item(text, item, lambda b: set_item_attr(b, 'thrust_damage', damage))
    for item, price in PRICES.items():
        text = edit_item(text, item, lambda b: set_item_attr(b, 'value', price))
    for item in UNPRICED:
        text = edit_item(text, item, drop_item_value)
    armours = {}
    for item in ET.fromstring(text.encode('utf-8')).iter('Item'):
        row = armour_row(item)
        if row:
            armours[item.get('id')] = row
        if item.get('Type') == 'BodyArmor':
            arm = item.find('.//Armor').get('arm_armor')
            cap = ARM_CAPS[row['arm']]
            if arm is not None and int(arm) > cap:
                text = edit_item(text, item.get('id'), lambda b: set_item_attr(b, 'arm_armor', cap))
    write(ARMOURS, text)

    firearms = read(FIREARMS)
    for item, damage in FIREARM_DAMAGE.items():
        firearms = edit_item(firearms, item, lambda b: drop_item_value(set_item_attr(b, 'thrust_damage', damage)))
    write(FIREARMS, firearms)
    return armours


def write_table(armours):
    tiers = {i: t for i, (_, t) in WEAPON_TIERS.items()}
    tiers.update(EXTRA_TIERS)
    lines = ['<?xml version="1.0" encoding="utf-8"?>',
             '<!-- Generated by tools/combat/apply_combat_data.py in DellarteDellaGuerra.Core. -->',
             '<CombatItems>']
    lines += ['  <Tier id="%s" tier="%d" />' % (i, t) for i, t in sorted(tiers.items())]
    lines += ['  <Armour id="%s" %s />' % (i, ' '.join('%s="%s"' % kv for kv in m.items()))
              for i, m in sorted(armours.items())]
    lines += ['</CombatItems>', '']
    write(TABLE, '\n'.join(lines))


def validate():
    errors = []
    for path in (PIECES, TEMPLATES, DESCRIPTIONS, WEAPONS, ARMOURS, FIREARMS, TABLE):
        try:
            ET.parse(path)
        except ET.ParseError as e:
            errors.append('%s: %s' % (path, e))
    if errors:
        sys.exit('\n'.join(errors))

    pieces = [n.get('id') for n in ET.parse(PIECES).getroot().iter('CraftingPiece')]
    if len(pieces) != len(set(pieces)):
        errors.append('duplicate crafting pieces')
    usable = {p.get('piece_id') for t in ET.parse(TEMPLATES).getroot().iter('CraftingTemplate')
              if t.get('id') == LONG_PIKE_TEMPLATE for p in t.iter('UsablePiece')}
    for usage in ET.parse(DESCRIPTIONS).getroot().iter('WeaponDescription'):
        if usage.get('id') in LONG_PIKE_USAGES and LONG_PIKE_HEAD not in {p.get('id') for p in usage.iter('AvailablePiece')}:
            errors.append('%s misses %s' % (usage.get('id'), LONG_PIKE_HEAD))
    if LONG_PIKE_HEAD not in usable:
        errors.append(LONG_PIKE_TEMPLATE + ' misses ' + LONG_PIKE_HEAD)

    known = {i.get('id') for p in (WEAPONS, ARMOURS, FIREARMS) for i in ET.parse(p).getroot().iter() if i.tag in ('Item', 'CraftedItem')}
    known |= {'battania_mace_1_t2', 'short_sword_t3'}
    root = ET.parse(TABLE).getroot()
    for node in root:
        if node.get('id') not in known:
            errors.append('table lists unknown item ' + node.get('id'))
    worn = ('BodyArmor', 'HeadArmor', 'HandArmor', 'LegArmor')
    body = {i.get('id') for i in ET.parse(ARMOURS).getroot().iter('Item') if i.get('Type') in worn}
    listed = {n.get('id') for n in root.iter('Armour')}
    errors += ['no material for ' + i for i in sorted(body - listed)]

    rows = simulate()
    for item, (family, tier) in WEAPON_TIERS.items():
        r = rows[item]
        swing, thrust = LADDER[family][0][tier - 1], LADDER[family][1][tier - 1]
        sf, tf = float(r['sf']), float(r['tf'])
        print('%-30s T%d %-10s W%.2f R%3s spd %3s/%3s  swing %3s/%3d %s  thrust %3s/%3d' % (
            item, tier, family, float(r['W']), r['R'], r['ss'], r['ts'], r['swd'], swing, r['st'], r['thd'], thrust))
        if swing and sf and abs(int(r['swd']) - swing) > 2 and r['bl'] not in SHARED_BLADES:
            errors.append('%s swing %s, wanted %d' % (item, r['swd'], swing))
        if thrust and tf and abs(int(r['thd']) - thrust) > 2 and r['bl'] not in SHARED_BLADES:
            errors.append('%s thrust %s, wanted %d' % (item, r['thd'], thrust))
    if errors:
        sys.exit('\n'.join(errors))
    print('valid:', len(pieces), 'pieces,', len(root), 'table rows')



split_long_pike_head()
apply_geometry_and_types()
solve_factors()
write_table(apply_item_data())
validate()
