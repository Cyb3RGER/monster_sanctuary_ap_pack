import json
from PyPopTracker.packs.items import PopTrackerToggleItem, export_items, PopTrackerConsumableItem, \
    PopTrackerToggleBadgedItem

from utils import format_code, count_flags, TAB

# ToDo: hardcoded for now
abilities_compact = [
    'Breakable Walls',
    'Impassible Vines',
    'Diamond Blocks',
    'Fire Orbs',
    'Water Orbs',
    'Lightning Orbs',
    'Earth Orbs',
    'Ice Orbs',
    'Distant Ice Orbs',
    'Fiery Shots',
    'Summon Rock',
    'Summon Mushroom',
    'Summon Big Rock',
    'Flying',
    'Improved Flying',
    'Lofty Mount',
    'Basic Swimming',
    'Improved Swimming',
    'Dual Mobility',
    'Narrow Corridors',
    'Magic Walls',
    'Magic Vines',
    'Heavy Blocks',
    'Torches',
    'Dark Rooms',
    'Grapple',
    'Levitate',
    'Secret Vision',
    'Basic Mount',
    'Sonar Mount',
    'Tar Mount',
    'Charging Mount',
    'Ghost Form'
]

# ToDo
ability_mapping = {
    'Blob Form': ['Narrow Corridors'],
    'Bubble Burst': ['Water Orbs'],
    'Charging Mount': ['Basic Mount', 'Charging Mount', 'Breakable Walls', 'Diamond Blocks'],
    'Claws': ['Breakable Walls', 'Impassible Vines'],
    'Corrosive Jabs': ['Breakable Walls', 'Water Orbs'],
    'Crush': ['Breakable Walls', 'Diamond Blocks'],
    'Dual Mobility': ['Dual Mobility', 'Flying', 'Improved Flying', 'Basic Swimming', 'Improved Swimming', 'Tar Mount'],
    'Fiery Shots': ['Fire Orbs', 'Fiery Shots'],
    'Flying': ['Flying'],
    'Freeze': ['Ice Orbs'],
    'Ghost Form': [],
    'Grapple': ['Grapple'],
    'Heavy Punch': ['Breakable Walls'],
    'Ignite': ['Impassible Vines', 'Torches', 'Fire Orbs'],
    'Improved Flying': ['Flying', 'Improved Flying'],
    'Improved Swimming': ['Basic Swimming', 'Improved Swimming'],
    'Jewel Blast': ['Earth Orbs'],
    'Levitate': ['Levitate'],
    'Light': ['Dark Rooms'],
    'Light Crush': ['Breakable Walls', 'Diamond Blocks', 'Dark Rooms'],
    'Lightning Bolt': ['Torches', 'Lightning Orbs'],
    'Lofty Mount': ['Lofty Mount'],
    'Minnesang': ['Magic Walls'],
    'Morph Ball': ['Narrow Corridors'],
    'Mount': ['Basic Mount'],
    'Secret Vision': ['Secret Vision'],
    'Shock Freeze': ['Ice Orbs', 'Lightning Orbs', 'Distant Ice Orbs'],
    'Slash': ['Breakable Walls', 'Impassible Vines'],
    'Slime Shot': ['Earth Orbs'],
    'Snowball Toss': ['Ice Orbs', 'Distant Ice Orbs'],
    'Sonar': ['Dark Rooms'],
    'Sonar Mount': ['Basic Mount', 'Dark Rooms', 'Sonar Mount'],
    'Spore Shroud': ['Magic Vines'],
    'Summon Big Rock': ['Summon Big Rock'],
    'Summon Mushroom': ['Summon Mushroom'],
    'Summon Rock': ['Summon Rock'],
    'Swimming': ['Basic Swimming'],
    'Tackle': ['Breakable Walls', 'Heavy Blocks'],
    'Tar Mount': ['Basic Mount', 'Tar Mount'],
    'Toxic Freeze': ['Ice Orbs', 'Earth Orbs'],  # ToDo: distant orbs as well?
    'Toxic Slam': ['Breakable Walls', 'Earth Orbs']
}


def gen_items():
    datastorage_ability_mapping: dict[str, tuple[list[str], str]] = {}
    datastorage_monster_mapping: dict[str, tuple[list[str], str]] = {}
    monster_ability_item_data = {}
    flag_counts = count_flags()
    with open('data/items.json', mode='r') as f:
        json_data = json.load(f)
    item_id: int = 970500
    item_mapping: dict[int, tuple[list[str], str]] = {}
    for type_data in json_data:
        item_type = type_data["type"]
        items = []
        type_classification = type_data.get("classification")
        for item_data in type_data["items"]:
            is_ability = item_type == "Explore Ability"
            is_egg = item_type == "Egg"
            is_costume = item_type == "Costume"
            classification = item_data.get("classification") or type_classification
            name = item_data["name"]
            # if is_ability:
            #     if "Ability - " in name:
            #         name = name[len("Ability - "):]
            #     name += " Unlock"
            main_code = format_code(name)
            if classification is None or classification == "filler" or classification == "trap" or is_costume or is_egg:
                item_id = item_id + 1
                continue
            codes = [main_code]
            groups = item_data.get('groups') or []
            if not is_egg:
                for code in groups:
                    code = format_code(code)
                    codes.append(code)
            count = item_data.get('count') or 1
            if item_type == "Flag" or item_type == "Rank":
                count = flag_counts[name] if name in flag_counts else 1
            if main_code == "mozzie":
                count = 15
            if is_ability:
                img = f'images/items/abilities/{main_code}.png'
            else:
                img = f'images/items/{format_code(item_type)}/{main_code}.png'
            is_key = "Area Key" in groups
            disabled_img_mods = None
            overlay_font_size = None
            if is_key:
                disabled_img_mods = ""
            if count == 1 and not is_key:
                item = PopTrackerToggleItem(name, codes=', '.join(codes), img=img)
            else:
                overlay_font_size = 24
                item = PopTrackerConsumableItem(name, codes=', '.join(codes), img=img,
                                                overlay_font_size=overlay_font_size,
                                                disabled_img_mods=disabled_img_mods, max_quantity=count)
            items.append(item)
            item_mapping[item_id] = ([main_code], item.type)
            item_id = item_id + 1
        if len(items) > 0:
            export_items(items, out_path=f'../items/{format_code(item_type)}.json')
            print(f'Exported {item_type.lower()} items!')
    with open('data/monsters.json', mode='r') as f:
        json_data = json.load(f)
    items = []
    for monster_data in json_data:
        name = monster_data["Name"]
        main_code = format_code(name)
        codes = [main_code]
        # for code in monster_data.get('Groups') or []:
        #     code = format_code(code)
        #     codes.append(code)
        #     if item_id in item_mapping:
        #         item_mapping[item_id][0].append(code)
        #     else:
        #         item_mapping[item_id] = ([code], "toggle")
        img = f'images/items/monsters/{main_code}.png'
        item = PopTrackerToggleItem(name, img=img, codes=', '.join(codes))
        items.append(item)
        datastorage_monster_mapping[name] = (codes, item.type)        
        monster_ability_item_data[main_code] = { k: format_code(v) for k,v in monster_data.get("AbilityLockItems", {}).items() }
    export_items(items, out_path=f'../items/monsters.json')
    print(f'Exported monsters items!')
    items = []
    for ability in abilities_compact:
        main_code = ability.lower().replace(' ', '_')
        img = f'images/items/abilities/{main_code}.png'
        codes = [main_code]
        # if main_code.startswith('basic_'):
        #     codes.append(main_code[6:])
        if main_code in ["flying", "improved_flying", "dual_mobility", "lofty_mount"]:
            codes.append("distant_ledges")
        if main_code in ["basic_swimming", "improved_swimming", "dual_mobility"]:
            codes.append("swimming")
        if "summon" in main_code:
            codes.append('ground_switches')
        if "mount" in main_code:
            codes.append("mount")
        if main_code in ["tar_mount", "dual_mobility"]:
            codes.append("tar")
        if main_code in ["charging_mount"]:
            codes.append("breakable_walls")
        if main_code.startswith('distant_'):
            codes.append(main_code[len('distant_'):])
        if main_code == 'distant_fire_orbs':
            codes.append('fiery_shots')

        item = PopTrackerToggleItem(ability, img=img, codes=', '.join(codes))
        items.append(item)
        codes = [code + '_locked' for code in codes]
        img = f'images/items/abilities/locked.png'
        item = PopTrackerToggleBadgedItem(ability + ' (Locked)', base_item=main_code, img=img,
                                          initial_active_state=True, codes=', '.join(codes))
        items.append(item)
    export_items(items, out_path=f'../items/abilities.json')
    print(f'Exported abilities items!')
    export_item_mapping(item_mapping)
    print(f'Exported item mappings!')
    # for k, v in ability_mapping.items():
    #     datastorage_ability_mapping[k] = ([format_code(v2) for v2 in v], 'toggle')
    # export_datastorage_item_mappings(datastorage_ability_mapping | datastorage_monster_mapping)
    export_datastorage_item_mappings(datastorage_monster_mapping)
    print(f'Exported datastorage mappings!')
    export_monster_ability_item_data(monster_ability_item_data)
    print(f'Exported monster ability item data!')
    monster_ability_prog_data = {}
    with open('data/progressive_explore_ability_unlocks.json', mode='r') as f:
        json_data = json.load(f)
    for prog_data in json_data:
        code = format_code(prog_data["ability"])
        prog_entry = prog_data.get("progression", None)
        combo_entry = prog_data.get("combo", None)
        current_data = {}
        if prog_entry:
            current_data["Progressive"] = {
                "Code": format_code(prog_entry["name"] ),
                "Amount": prog_entry["quantity"]
            }
        else:
            print(f'!!! NO Prog Entry for Ability {code} !!!')
        if combo_entry:
            current_data["Combo"] = [
                {
                    "Code": format_code(v["name"] ),
                    "Amount": v["quantity"]
                } for v in combo_entry
            ]
        else:
            print(f'!!! NO Prog Entry for Ability {code} !!!')
        monster_ability_prog_data[code] = current_data
    export_monster_ability_prog_data(monster_ability_prog_data)
    print(f'Exported monster ability prog data!')


def export_monster_ability_prog_data(monster_ability_prog_data):
    lines = ['MONSTER_ABILITY_PROG_DATA = {']
    for i, (k, v) in enumerate(monster_ability_prog_data.items()):
        line = f'{TAB}["{k}"] = {{ '
        lines.append(line)
        prog_entry = v.get('Progressive', None)
        if prog_entry:
            line = f'{TAB*2}Progressive = {{ Code = \"{prog_entry["Code"]}\", Amount = {prog_entry["Amount"]} }},'
            lines.append(line)
        combo_entry = v.get('Combo', None)
        if combo_entry:
            line = f'{TAB*2}Combo = {{'
            lines.append(line)
            for j, v2 in enumerate(combo_entry):
                line = f'{TAB*3}{{ Code = \"{v2["Code"]}\", Amount = {v2["Amount"]} }}'
                if j != len(combo_entry) - 1:
                    line += ','                
                lines.append(line)
            lines.append(f'{TAB*2}}}')
        line = f'{TAB}}}'
        if i != len(monster_ability_prog_data) - 1:
            line += ','
        lines.append(line)
    lines.append('}')

    with open('../scripts/logic/monster_ability_prog_data.lua', mode='w') as f:
        f.write('\n'.join(lines))
def export_monster_ability_item_data(monster_ability_item_data):
    lines = ['MONSTER_ABILITY_ITEM_DATA = {']
    for i, (k, v) in enumerate(monster_ability_item_data.items()):
        line = f'{TAB}["{k}"] = {{ '
        for j, (k2, v2) in enumerate(v.items()):
            line += f'{k2} = "{v2}"'
            if j != len(v)-1:
                line += ', '
        line += f' }}'
        if i != len(monster_ability_item_data) - 1:
            line += ','
        lines.append(line)
    lines.append('}')

    with open('../scripts/logic/monster_ability_item_data.lua', mode='w') as f:
        f.write('\n'.join(lines))


def export_datastorage_item_mappings(datastorage_mapping: dict[str, tuple[list[str], str]]):
    lines = ['DATASTORAGE_ITEM_MAPPING = {']
    for k, v in datastorage_mapping.items():
        line = f'{TAB}["{k}"] = {{{{'
        for i in v[0]:
            line += f'"{i}"'
            if i != v[0][len(v[0]) - 1]:
                line += ', '
        line += f'}}, "{v[1]}"}},'
        lines.append(line)
    lines.append('}')

    with open('../scripts/autotracking/datastorage_mapping.lua', mode='w') as f:
        f.write('\n'.join(lines))


def export_datastorage_ability_mapping(datastorage_ability_mapping: dict[str, list[str]]):
    lines = ['DATASTORAGE_ABILITY_MAPPING  = {']
    for k, v in datastorage_ability_mapping.items():
        line = f'{TAB}["{k}"] = {{{{'
        for i in v[0]:
            line += f'"{i}"'
            if i != v[0][len(v[0]) - 1]:
                line += ', '
        line += f'}}, "{v[1]}"}},'
        lines.append(line)
    lines.append('}')

    with open('../scripts/autotracking/datastorage_mapping.lua', mode='w') as f:
        f.write('\n'.join(lines))


def export_item_mapping(ids_for_items: dict[int, (list[str], str)]):
    lines = ['ITEM_MAPPING = {']
    for k, v in ids_for_items.items():
        line = f'{TAB}[{k}] = {{{{'
        for i in v[0]:
            line += f'"{i}"'
            if i != v[0][len(v[0]) - 1]:
                line += ', '
        line += f'}}, "{v[1]}"}},'
        lines.append(line)
    lines.append('}')

    with open('../scripts/autotracking/item_mapping.lua', mode='w') as f:
        f.write('\n'.join(lines))


if __name__ == "__main__":
    gen_items()
