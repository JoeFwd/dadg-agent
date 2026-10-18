---
name: dadg-add-a-cannon-howto
description: Adding a cannon to DADG is data-driven: cannons.xml, siege_engines.xml, cannon_items.xml, prefabs, FBX meshes, three UI sprites, scene spawners.
type: howto
topic: feature-cannons
tags: [cannons, howto, data-driven]
sources: [doc/adding-a-cannon.md]
updated: 2026-10-18
---

# Dadg add a cannon howto

No C# is needed; the id in `ModuleData/CustomXml/cannons.xml` creates a `GenericCannon_<id>` script type at startup. Copy the falconet as reference. Steps:
1. `cannons.xml` entry: `Id` (letter then alphanumerics), icons, `MachineType` > 7 unique (falconet 8), map prefab, bone index 0. Invalid entries are logged and skipped.
2. `Cannons/siege_engines.xml`: damage, hit chance, `man_day_cost`, `campaign_rate_of_fire_per_day` (falconet 200 damage, 0.52, 12, 20).
3. `Cannons/cannon_items.xml`: `<id>_cannonball`, weapon_class Boulder, reuse `small_cannonball` and the `cannonball` physics material.
4. Meshes in `AssetSources/cannons/cannons.fbx`: `dadg_siege_<id>_base/_barrel/_wheel_r/_wheel_l` and physics `bo_dadg_siege_<id>`; recompile `cannons_geo.tpac`.
5. `Prefabs/cannons.xml`: `dadg_<id>`, `_mapicon`, `_ghost`, `_spawner`. Script variables: `SiegeEngineId`, `MissileItemID`, `BaseMuzzleVelocity` (120), `startingAmmoCount` (20), elevation limits 0.2 and -0.1 rad, `Focus`, `PreferHighAngle`, native mangonel animations. Destructible `MaxHitPoint` 350.
6. Scenes: place the spawner per [[siege-spawner-scene-requirements]] and [[siege-spawner-forward-axis-must-face-away-from-walls]].
7. Three sprites (146x146, 30x23, 52x52) via [[gauntlet-sprite-atlas-repack-workflow]]; sounds in `Cannons/sounds.xml` with category `mission_siege_loud`.
Verify: log shows `Loaded cannon: <id>`, campaign icon, ghost preview, firing effects, destroyed state, map animation. The cannon sprite source folder is `DadgMainUISpriteParts`-separate on purpose.

Source docs: doc/adding-a-cannon.md.

Related: [[campaign-siege-engine-registration-numbers]]
