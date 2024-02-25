import json
from PyPopTracker.packs.items import PopTrackerToggleItem, export_items, PopTrackerConsumableItem

from utils import format_code, count_flags

# ToDo: hardcoded for now
abilities = [
    'Breakable Walls',
    'Impassible Vines',
    'Diamond Blocks',
    'Fire Orbs',
    'Water Orbs',
    'Lightning Orbs',
    'Earth Orbs',
    'Ice Orbs',
    'Distant Ice Orbs',
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
    'Fiery Shots',
    'Heavy Blocks',
    'Torches',
    'Dark Rooms',
    'Grapple',
    'Levitate',
    'Secret Vision',
    'Spore Shroud',
    'Basic Mount',
    'Sonar Mount',
    'Tar Mount',
    'Charging Mount'
]


def gen_items():
    datastorage_mapping = {}
    flag_counts = count_flags()
    with open('data/items.json', mode='r') as f:
        json_data = json.load(f)
    item_id: int = 970500
    item_mapping: dict[int, tuple[list[str], str]] = {}
    for type_data in json_data:
        item_type = type_data["type"]
        items = []
        for item_data in type_data["items"]:
            is_ability = item_type == "Ability"
            is_egg = item_type == "Egg"
            classification = item_data.get("classification")
            name = item_data["name"]
            if is_ability:
                name = name[len("Ability - "):]
            main_code = format_code(name)
            if classification is None or classification == "filler" or (
                    is_egg and main_code != 'dodo_egg') or is_ability:
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
            if is_ability:
                pass
                # abilities.append(item)
            else:
                items.append(item)
                item_mapping[item_id] = ([main_code], item.type)
            item_id = item_id + 1
        if len(items) > 0:
            export_items(items, out_path=f'../items/{format_code(item_type)}.json')
            print(f'Exported {item_type.lower()} items!')
    # with open('data/monsters.json', mode='r') as f:
    #     json_data = json.load(f)
    # items = []
    # for monster_data in json_data:
    #     name = monster_data["Name"]
    #     main_code = format_code(name)
    #     codes = [main_code]
    #     for code in monster_data.get('Groups') or []:
    #         code = format_code(code)
    #         codes.append(code)
    #         if item_id in item_mapping:
    #             item_mapping[item_id][0].append(code)
    #         else:
    #             item_mapping[item_id] = ([code], "toggle")
    #     img = f'images/items/monsters/{main_code}.png'
    #     item = PopTrackerToggleItem(name, img=img, codes=', '.join(codes))
    #     items.append(item)
    #     item_mapping[item_id] = (codes, item.type)
    #     item_id = item_id + 1
    # monsters = items.copy()
    # export_items(items, out_path=f'../items/monsters.json')
    # print(f'Exported monsters items!')
    items = []
    for ability in abilities:
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

        item = PopTrackerToggleItem(ability, img=img, codes=', '.join(codes))
        items.append(item)
        datastorage_mapping[ability] = [[main_code], "toggle"]
    export_items(items, out_path=f'../items/abilities.json')
    print(f'Exported abilities items!')
    # codes = [[]]
    # i = 0
    # j = 0
    # for item in items:
    #     codes[i].append(item.codes.split(",")[0])
    #     j += 1
    #     if j % 9 == 0:
    #         i += 1
    #         codes.append([])
    # print(json.dumps(codes))
    export_item_mapping(item_mapping)
    export_datastorage_mapping(datastorage_mapping)
    print(f'Exported item mappings!')

def export_datastorage_mapping(datastorage_mapping: dict[str, list[str]]):
    lines = ['DATASTORAGE_MAPPING = {']
    for k, v in datastorage_mapping.items():
        line = f'\t["{k}"] = {{{{'
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
        line = f'\t[{k}] = {{{{'
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
