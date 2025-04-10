import json

from gen_items import abilities_compact
from utils import format_code, count_flags, TAB

open_rules: dict[str, dict[str, list[str | int]]] = {
    'open_blue_caves': {
        'blue_cave_champion_room_2_west_shortcut': [1]
    },
    'open_stronghold_dungeon': {
        'stronghold_dungeon_south_3_shortcut': [2, 3],
        'stronghold_dungeon_west_4_shortcut': [1, 3],
    },
    'open_snowy_peaks': {
        'snowy_peaks_east4_upper_shortcut': [1],
        'snowy_peaks_east_mountain_3_shortcut': [1]
    },
    'open_sun_palace': {
        'snowy_peaks_sun_palace_entrance_shortcut': [1, 3],
        'sun_palace_raise_center_1': [2, 3],
        'sun_palace_raise_center_2': [2, 3],
        'sun_palace_raise_center_3': [2, 3],
        'sun_palace_lower_water_1': [2, 3],
        'sun_palace_lower_water_2': [2, 3],
        'sun_palace_east_shortcut': [2, 3],
        'sun_palace_west_shortcut': [2, 3],
    },
    'open_ancient_woods': {
        'ancient_woods_east_shortcut': [1],
        'ancient_woods_brutus_access': [1],
    },
    'open_horizon_beach': {
        'ancient_woods_beach_access': [1, 3],
        'horizon_beach_center_shortcut': [2, 3],
        'horizon_beach_to_magma_chamber_shortcut': [1, 3],
    },
    'open_magma_chamber': {
        'ancient_woods_magma_chamber_shortcut': [1, 3],
        'magma_chamber_north_shortcut': [2, 3],
        'magma_chamber_center_shortcut': [2, 3],
        'magma_chamber_east_shortcut': [2, 3],
        'magma_chamber_south_shortcut': [2, 3],
        'magma_chamber_lower_lava': [2, 3],
        'magma_chamber_forgotten_world_access': [1, 3],
    },
    'open_forgotten_world': {
        'forgotten_world_to_horizon_beach_shortcut': [1, 3],
        'forgotten_world_to_magma_chamber_shortcut': [1, 3],
        'forgotten_world_caves_shortcut': [2, 3],
        'forgotten_world_waters_shortcut': [2, 3],
    },
    'open_underworld': {
        'underworld_east_catacomb_8_shortcut': [2, 3],
        'underworld_east_catacomb_6_shortcut': [2, 3],
        'underworld_west_catacomb_4_shortcut': [2, 3],
        'underworld_west_catacomb_7_shortcut': [2, 3],
        'underworld_west_catacomb_roof_access': [2, 3],
        'underworld_to_sun_palace_shortcut': [1, 3],
        'all_sanctuary_tokens': [1, 3],
    },
    'open_mystical_workshop': {
        'mystical_workshop_north_shortcut': [1]
    },
    'open_abandoned_tower': {
        'abandoned_tower_access': [1, 3],
        'abandoned_tower_south_shortcut': [2, 3],
        'abandoned_tower_center_shortcut': [2, 3],
        'key_of_power': [1, 3],
    },
    'open_blob_burg': {
        'all_blob_keys_used': [1, 3],
        'blob_burg_access_1': [2, 3],
        'blob_burg_access_2': [2, 3],
        'blob_burg_access_3': [2, 3],
        'blob_burg_access_4': [2, 3],
        'blob_burg_access_5': [2, 3],
        'blob_burg_access_6': [2, 3],
    }
}

monster_ability_rules: dict[str, list[str]] = {
    "claws": [
        "spectral_wolf",
        "spectral_lion",
        "molebear",
    ],
    "tackle": [
        "spectral_toad",
        "yowie",
        "steam_golem",
        "vasuki",
        "brawlish",
        "targoat",
    ],
    "slash": [
        "catzerker",
        "minitaur",
        "blade_widow",
        "ucan",
    ],
    "heavy_punch": [
        "monk",
    ],
    "toxic_slam": [
        "goblin_brute",
    ],
    "light_crush": [
        "goblin_miner",
    ],
    "crush": [
        "salahammer",
        "asura",
        "goblin_pilot",
        "darnation",
    ],
    "corrosive_jabs": [
        "troll",
    ],
    "charging_mount": [
        "rampede",
        "rathops",
    ],
    "ignite": [
        "magmapillar",
        "tengu",
        "specter",
        "magmamoth",
        "imori",
        "lava_blob",
        "skorch",
        "plague_egg",
    ],
    "fiery_shots": [
        "goblin_hood",
        "polterofen",
        "mimic",
    ],
    "bubble_burst": [
        "blob",
        "grummy",
        "grulu",
    ],
    "lightning_bolt": [
        "crackle_knight",
        "beetloid",
        "goblin_warlock",
        "sizzle_knight",
    ],
    "shock_freeze": [
        "shockhopper",
    ],
    "slime_shot": [
        "toxiquus",
        "ninki",
        "ninki_nanka",
    ],
    "jewel_blast": [
        "goblin_king",
        "crystal_snail",
    ],
    "toxic_freeze": [
        "spinner",
    ],
    "freeze": [
        "ice_blob",
        "megataur",
    ],
    "snowball_toss": [
        "mogwai",
    ],
    "flying": [
        "spectral_eagle",
        "vaero",
        "frosty",
        "mad_eye",
        "raduga",
        "draconov",
    ],
    "improved_flying": [
        "silvaero",
        "kongamato",
        "dracogran",
        "dracozul",
        "draconoir",
        "ornithopter",
    ],
    "lofty_mount": [
        "gryphonix",
    ],
    "basic_swimming": [
        "koi",
    ],
    "improved_swimming": [
        "thornish",
        "nautilid",
        "elderjel",
        "dracomer",
    ],
    "dual_mobility": [
        "krakaturtle",
    ],
    "basic_mount": [
        "aurumtail",
        "qilin",
        "dodo",
        "moccus",
    ],
    "sonar_mount": [
        "akhlut",
    ],
    "tar_mount": [
        "tar_blob",
    ],
    "summon_rock": [
        "rocky",
        "druid_oak",
        "kame",
    ],
    "summon_mushroom": [
        "fungi",
        "tanuki",
    ],
    "summon_big_rock": [
        "brutus",
        "mega_rock",
        "promethean",
    ],
    "sonar": [
        "nightwing",
    ],
    "light": [
        "glowfly",
        "caraglow",
        "manticorb",
        "glowdra",
    ],
    "ghost_form": [
        "sycophantom",
        "kanko",
        "stolby",
    ],
    "spore_shroud": [
        "fumagus",
        "amberlgna",
    ],
    "grapple": [
        "oculus",
        "argiope",
        "arachlich",
        "worm",
    ],
    "blob_form": [
        "rainbow_blob",
        "king_blob",
    ],
    "morph_ball": [
        "changeling",
    ],
    "levitate": [
        "vodinoy",
        "diavola",
        "vertraag",
        "terradrile",
    ],
    "secret_vision": [
        "sutsune",
        "thanatos",
        "aazerach",
        "mad_lord",
        "ascendant",
    ],
    "minnesang": [
        "bard",
    ],
}

exploration_obstacle_rules = {
    "distant_ledges": [
        "flying",
        "improved_flying",
        "dual_mobility",
        "lofty_mount",
    ],
    "ground_switches": [
        "summon_big_rock",
        "summon_rock",
        "summon_mushroom",
    ],
    "swimming": [
        "basic_swimming",
        "improved_swimming",
        "dual_mobility",
    ],
    "mount": [
        "basic_mount",
        "sonar_mount",
        "tar_mount",
        "charging_mount",
        "lofty_mount",
    ],
    "tar": [
        "tar_mount",
        "dual_mobility"
    ],
    "breakable_walls": [
        "claws",
        "tackle",
        "slash",
        "heavy_punch",
        "toxic_slam",
        "light_crush",
        "crush",
        "corrosive_jabs",
        "charging_mount",
    ],
    "impassible_vines": [
        "claws",
        "ignite",
        "slash",
        "fiery_shots",
    ],
    "diamond_blocks": [
        "light_crush",
        "crush",
        "charging_mount"
    ],
    "fire_orbs": [
        "ignite",
        "fiery_shots",
    ],
    "water_orbs": [
        "bubble_burst",
        "corrosive_jabs",
    ],
    "lightning_orbs": [
        "lightning_bolt",
        "shock_freeze",
    ],
    "earth_orbs": [
        "slime_shot",
        "toxic_slam",
        "jewel_blast",
        "toxic_freeze",
    ],
    "ice_orbs": [
        "freeze",
        "snowball_toss",
        "shock_freeze",
        "toxic_freeze",
    ],
    "distant_ice_orbs": [
        "snowball_toss",
        "shock_freeze",
        "toxic_freeze",
    ],
    "narrow_corridors": [
        "blob_form",
        "morph_ball",
    ],
    "magic_walls": [
        "minnesang",
    ],
    "magic_vines": [
        "spore_shroud",
    ],
    "heavy_blocks": [
        "tackle",
    ],
    "torches": [
        "ignite",
        "lightning_bolt",
        "fiery_shots"
    ],
    "dark_rooms": [
        "sonar",
        "light",
        "sonar_mount",
        "light_crush",
    ],
}


def gen_logic():
    gen_item_helpers()
    gen_regions_table()
    gen_abilities_list()
    gen_monster_to_abilities()
    gen_evo_table()


def gen_evo_table():
    evo_table = {}
    child_table = {}
    with open('data/monsters.json', mode='r') as f:
        json_data = json.load(f)
    for monster_data in json_data:
        name = monster_data["Name"]
        main_code = format_code(name)
        evos = monster_data.get("Evolutions",[])
        for evo in evos:                
            evo_code = format_code(evo["Monster"])
            cata_code = format_code(evo["Catalyst"])
            if main_code not in evo_table:
                evo_table[main_code] = []
            evo_table[main_code].append((evo_code, cata_code))
            if not evo_code in child_table:
                child_table[evo_code] = []
            child_table[evo_code].append(main_code)
    lua_str = "EVO_TABLE = {\n"
    for k, vals in evo_table.items():
        lua_str += f"{TAB}[\"{k}\"] = {{"
        for v in vals:
            lua_str += f'{{ Monster = \"{v[0]}\", Catalyst = \"{v[1]}\" }}'
            if v != vals[-1]:
                lua_str += ", "
        lua_str += "},\n"
    lua_str += "}"
    lua_str += "\n\nCHILD_TABLE = {\n"
    for k, vals in child_table.items():
        lua_str += f"{TAB}[\"{k}\"] = {{"
        for v in vals:
            lua_str += f'"{v}"'
            if v != vals[-1]:
                lua_str += ", "
        lua_str += "},\n"
    lua_str += "}"
    with open('../scripts/logic/evo_table.lua', mode='w') as f:
        f.write(lua_str)


def map_monsters_to_abilities():
    mapping = {}
    for ability_name in abilities_compact:
        ability = format_code(ability_name)
        mons = []
        tmp = []
        if ability in exploration_obstacle_rules:
            tmp = exploration_obstacle_rules[ability]
        if ability in monster_ability_rules:
            tmp.append(ability)
        for v in tmp:
            mons += monster_ability_rules[v]
        mapping[ability] = mons
    inv_mapping = {}
    for ability, mons in mapping.items():
        for mon in mons:
            if mon not in inv_mapping:
                inv_mapping[mon] = []
            if ability not in inv_mapping[mon]:
                inv_mapping[mon].append(ability)
    return mapping, inv_mapping


def gen_monster_to_abilities():
    _, inv_mapping = map_monsters_to_abilities()
    lua_str = "MONSTERS_TO_ABILITIES = {\n"
    for k, vals in inv_mapping.items():
        lua_str += f"{TAB}[\"{k}\"] = {{"
        for v in vals:
            lua_str += f'"{v}"'
            if v != vals[-1]:
                lua_str += ", "
        lua_str += "},\n"
    lua_str += "}"
    with open('../scripts/logic/monsters_to_abilities.lua', mode='w') as f:
        f.write(lua_str)


def gen_abilities_list():
    lua_str = "ABILITIES_COMPACT = {\n"
    for v in abilities_compact:
        code = format_code(v)
        lua_str += f"{TAB}\"{code}\""
        if v != abilities_compact[-1]:
            lua_str += ",\n"
    lua_str += "\n}"
    with open('../scripts/logic/abilities_compact.lua', mode='w') as f:
        f.write(lua_str)


def gen_item_helpers():
    flag_counts = count_flags()
    # with open('data/plotless.json', mode='r') as f:
    #     plotless_data = json.load(f)
    # plotless_data = [data for data in plotless_data if data["type"] == "flag"]
    with open('data/items.json', mode='r') as f:
        json_data = json.load(f)
    codes = []
    code_to_type = {}
    for type_data in json_data:
        item_type = type_data["type"]
        is_ability = item_type == "Explore Ability"
        is_egg = item_type == "Egg"
        if is_ability:
            continue
        for item_data in type_data["items"]:
            classification = item_data.get("classification")
            if classification is None or classification == "filler":
                continue
            name = item_data["name"]
            # if name.startswith('Ability - '):
            #     name = name[len('Ability - '):]
            main_code = format_code(name)
            if main_code not in codes:
                codes.append(main_code)
            if not is_egg:
                for code in item_data.get('groups') or []:
                    code = format_code(code)
                    if code not in codes:
                        codes.append(code)
            count = item_data.get('count') or 1
            if item_type == "Flag" or item_type == "Rank":
                count = flag_counts[name] if name in flag_counts else 1
            is_consumable = count > 1
            if is_consumable:
                code_to_type[main_code] = "consumable"
        # for code in monster_data.get('Groups') or []:
        #     code = format_code(code)
        #     if code not in codes:
        #         codes.append(code)
    mon_codes = []
    evo_table = {}
    with open('data/monsters.json', mode='r') as f:
        json_data = json.load(f)
    for monster_data in json_data:
        name = monster_data["Name"]
        main_code = format_code(name)
        if main_code not in mon_codes:
            mon_codes.append(main_code)
    lua_str = ''
    # abilities = [format_code(v) for v in abilities_compact]
    for code in codes:
        lua_str += build_item_helper(code, code_to_type[code] if code in code_to_type else 'toggle')
    for code in mon_codes:
        lua_str += build_mon_helper(code, code_to_type[code] if code in code_to_type else 'toggle')
    for k, v in monster_ability_rules.items():
        lua_str += build_ability_helper(k, v)
        # lua_str += build_ability_helper(k, v, True)
    for k, v in exploration_obstacle_rules.items():
        lua_str += build_exploration_obstacle_helper(k, v)
        # lua_str += build_exploration_obstacle_helper(k, v, True)
    with open('data/world.json', mode='r') as f:
        json_data = json.load(f)
    for region_data in json_data:
        region_name = region_data["region"]
        flags = region_data.get('flags') or []
        for flag in flags:
            flag_id = flag['id']
            flag_requirements = flag.get('requirements') or []
            # plotless_flag_data = next((x for x in plotless_data if x['id'] == flag_id), None)
            # if plotless_flag_data is not None and len(plotless_flag_data['requirements']) > 0:
            #     flag_requirements = ['OR',
            #                          ['AND', ['skip_plot'] + plotless_flag_data['requirements']] + flag_requirements]
            lua_str += build_flag_helper(format_code(flag_id), region_name, flag_requirements)
    for k, _ in open_rules.items():
        lua_str += build_slot_data_func(k)
    with open('../scripts/logic/logic_generated.lua', mode='w') as f:
        f.write(lua_str)
    print('logic helpers done!')
        


def build_slot_data_func(opt_name):
    lua_str = f'function {opt_name}(val)\n'
    lua_str += f'{TAB}if SLOT_DATA == nil then\n{TAB * 2}return false\n{TAB}end\n'
    lua_str += f'{TAB}return SLOT_DATA.options.{opt_name} == val\n'
    lua_str += 'end\n\n'
    return lua_str


def format_func_value(v):
    if isinstance(v, str):
        return f"\"{v}\""
    return f"{v}"


def build_flag_helper(code, region, req_data):
    # ToDo: we could make optimize_req_data function
    #       to pull multiple occurrences of a requirement in all ANDs with an OR out and similar
    func_name = code
    access_req = [f'has_access_to(\'{region}\')']
    if not req_data:
        req_actual = access_req
    else:
        req_actual = ['AND', access_req + req_data]
    for open_rule_name, open_rule in open_rules.items():
        if code in open_rule:
            req_actual = ['OR', req_actual + [f"{open_rule_name}({format_func_value(v)})" for v in open_rule[code]]]
    lua_str = f'function {func_name}()\n'
    lua_str += build_access_func(req_actual, 1)
    lua_str += 'end\n\n'
    return lua_str


def build_ability_helper(ability, monsters, useHas=False):
    func_name = ('has_' if useHas else '') + ability
    lua_str = f'function {func_name}()\n'
    lua_str += f'{TAB}return '
    lua_str += f"can_use_ability(\'{ability}\')"
    # for v in monsters:
    #     lua_str += f'{v}()' if useHas else f"can_use_ability(\'{v}\')"
    #     # lua_str += f'{(v if useHas else "can_use_ability")}(\'{("" if useHas else v)}\')'
    #     if v != monsters[-1]:
    #         lua_str += ' or '
    lua_str += '\nend\n\n'
    return lua_str


def build_exploration_obstacle_helper(obstacle, abilities, useHas=False):
    func_name = ('has_' if useHas else '') + obstacle
    lua_str = f'function {func_name}()\n'
    lua_str += f'{TAB}return '
    lua_str += f"can_use_ability(\'{obstacle}\')"
    for v in abilities:
        lua_str += ' or '
        lua_str += f'{("has_" if useHas else "") + v}()'
    lua_str += '\nend\n\n'
    return lua_str


def build_item_helper(code, item_type='toggle'):
    func_name = code
    lua_str = f'function {func_name}('
    if item_type == 'consumable':
        lua_str += 'n'
    lua_str += ')\n'
    lua_str += f'{TAB}return has(\'{code}\''
    if item_type == 'consumable':
        lua_str += ', n'
    lua_str += ')'
    for open_rule_name, open_rule in open_rules.items():
        if code in open_rule:
            for v in open_rule[code]:
                # ToDo: this should technically use _OR
                lua_str += f' or {open_rule_name}({format_func_value(v)})'
    lua_str += '\nend\n\n'
    return lua_str

def build_mon_helper(code, item_type='toggle'):
    func_name = code
    lua_str = f'function {func_name}('
    if item_type == 'consumable':
        lua_str += 'n'
    lua_str += ')\n'
    lua_str += f'{TAB}return has_mon_full(\'{code}\')'
    lua_str += '\nend\n\n'
    return lua_str


def gen_regions_table():
    with open('data/world.json', mode='r') as f:
        world_data = json.load(f)
    # with open('data/plotless.json', mode='r') as f:
    #     plotless_data = json.load(f)
    # for data in plotless_data:
    #     loc_type = data['type']
    #     if loc_type != 'connection':
    #         continue
    #     region_name = data['region']
    #     con_name = data['connection']
    #     region_data = next((v for v in world_data if v['region'] == region_name), None)
    #     con_data = next((v for v in region_data['connections'] if v['region'] == con_name), None)
    #     if len(data['requirements']) > 0:
    #         con_data['requirements'] = ['OR', ['AND', ['skip_plot'] + data['requirements']] + con_data['requirements']]
    #     else:
    #         con_data['requirements'] = ['OR', ['skip_plot'] + con_data['requirements']]
    lua_str = 'REGIONS = {\n'
    for i, region in enumerate(world_data):
        lua_str += f'{TAB}["{region["region"]}"] = {{\n'
        conn_data = region.get("connections")
        for i, conn in enumerate(conn_data):
            # Hack because we store comments as strings
            if isinstance(conn, str):
                continue
            lua_str += f'{TAB * 2}["{conn["region"]}"] = function()\n'
            req_data = conn.get('requirements') or []
            lua_str += build_access_func(req_data, 3)
            lua_str += f'{TAB * 2}end'
            if i != len(conn_data) - 1:
                lua_str += ','
            lua_str += '\n'
        lua_str += f'{TAB}}}'
        if i != len(world_data) - 1:
            lua_str += f','
        lua_str += '\n'
    lua_str += '}\n'
    with (open('../scripts/logic/regions.lua', mode='w') as lf):
        lf.write(lua_str)
    print('regions table done!')


def build_access_func(req_data, tab_depth):
    if len(req_data) == 0:
        return f'{TAB * tab_depth}return true\n'
    if len(req_data) == 1:
        return f'{TAB * tab_depth}return {format_req(req_data[0])}\n'
    if len(req_data) == 2 and req_data[0] == "AND" or req_data[0] == "OR":
        return f'{TAB * tab_depth}return\n{build_access_func_part(req_data[1], tab_depth, req_data[0])}\n'
    return f'{TAB * tab_depth}return\n{build_access_func_part(req_data, tab_depth)}\n'


def build_access_func_part(req_data, tab_depth, op="AND"):
    lua_str = ''
    lua_str += f'{TAB * tab_depth}_{op}({{\n'
    skip_next = False
    for i in range(0, len(req_data)):
        if skip_next:
            skip_next = False
            continue
        if req_data[i] == "AND" or req_data[i] == "OR":
            lua_str += build_access_func_part(req_data[i + 1], tab_depth + 1, req_data[i])
            skip_next = True
            if i + 1 != len(req_data) - 1:
                lua_str += ','
            lua_str += '\n'
        else:
            lua_str += f'{TAB * (tab_depth + 1)}'
            lua_str += format_req(req_data[i])
            if i != len(req_data) - 1:
                lua_str += ','
            lua_str += '\n'
    lua_str += f'{TAB * tab_depth}}})'
    return lua_str


def format_req(req):
    is_func = '(' in req and ')' in req
    result: str
    if req.startswith('NOT '):
        result = f'_NOT({req[4:]}{"" if is_func else "()"})'
    else:
        result = f'{req}{"" if is_func else "()"}'
    return result


if __name__ == "__main__":
    gen_logic()
