import json

from utils import format_code, count_flags

TAB = '  '


def gen_logic():
    gen_item_helpers()
    gen_regions_table()


def gen_item_helpers():
    flag_counts = count_flags()
    with open('data/items.json', mode='r') as f:
        json_data = json.load(f)
    codes = []
    code_to_type = {}
    for type_data in json_data:
        item_type = type_data["type"]
        # ToDo: figure out which flags are double
        # if item_type == "Flag":
        #     continue
        for item_data in type_data["items"]:
            classification = item_data.get("classification")
            if classification is None or classification == "filler":
                continue
            name = item_data["name"]
            if name.startswith('Ability - '):
                name = name[len('Ability - '):]
            main_code = format_code(name)
            if main_code not in codes:
                codes.append(main_code)
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
    with open('data/monsters.json', mode='r') as f:
        json_data = json.load(f)
    for monster_data in json_data:
        name = monster_data["Name"]
        main_code = format_code(name)
        if main_code in codes:
            codes.append(main_code)
        for code in monster_data.get('Groups') or []:
            code = format_code(code)
            if code in codes:
                codes.append(code)
    lua_str = ''
    for code in codes:
        lua_str += build_item_helper(code, code_to_type[code] if code in code_to_type else 'toggle')
    with open('data/world.json', mode='r') as f:
        json_data = json.load(f)
    for region_data in json_data:
        region_name = region_data["region"]
        flags = region_data.get('flags') or []
        for flag in flags:
            lua_str += build_flag_helper(format_code(flag['id']), region_name, flag.get('requirements') or [])
    with open('../scripts/logic/logic_generated.lua', mode='w') as f:
        f.write(lua_str)
    print('logic helpers done!')


def build_flag_helper(code, region, req_data):
    func_name = code
    if not req_data:
        req_actual = [f'has_access_to(\'{region}\')']
    else:
        req_actual = ['AND', [f'has_access_to(\'{region}\')'] + req_data]
    lua_str = f'function {func_name}()\n'
    lua_str += build_access_func(req_actual,1)
    lua_str += 'end\n\n'
    return lua_str


def build_item_helper(code, item_type='toggle'):
    func_name = code
    lua_str = f'function {func_name}('
    if item_type == 'consumable':
        lua_str += 'n'
    lua_str += ')\n'
    lua_str += f'  return has(\'{code}\''
    if item_type == 'consumable':
        lua_str += ', n'
    lua_str += ')\nend\n\n'
    return lua_str


def gen_regions_table():
    with open('data/world.json', mode='r') as f:
        world_data = json.load(f)
    with open('data/plotless.json', mode='r') as f:
        plotless_data = json.load(f)
    for data in plotless_data:
        loc_type = data['type']
        if loc_type != 'connection':
            continue
        region_name = data['region']
        con_name = data['connection']
        region_data = next((v for v in world_data if v['region'] == region_name), None)
        con_data = next((v for v in region_data['connections'] if v['region'] == con_name), None)
        if len(data['requirements']) > 0:
            con_data['requirements'] = ['OR', ['AND', ['plotless'] + data['requirements']] + con_data['requirements']]
        else:
            con_data['requirements'] = ['OR', ['plotless'] + con_data['requirements']]
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
                lua_str += ', '
            lua_str += '\n'
        else:
            lua_str += f'{TAB * (tab_depth + 1)}'
            lua_str += format_req(req_data[i])
            if i != len(req_data) - 1:
                lua_str += ', '
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
