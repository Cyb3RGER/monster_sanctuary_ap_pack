import json
import re

TAB = ' ' * 4


def count_flags():
    flag_counts = {
        "Champion Defeated": 0
    }
    with open('data/world.json', mode='r') as f:
        json_data = json.load(f)
    for region_data in json_data:
        for flag_data in region_data.get("flags") or []:
            # Hack because we store comments as strings
            if isinstance(flag_data, str):
                continue
            flag_name = flag_data["name"]
            if flag_name not in flag_counts:
                flag_counts[flag_name] = 1
            else:
                flag_counts[flag_name] += 1
        for champion_data in region_data.get("champion") or []:
            # Hack because we store comments as strings
            if isinstance(champion_data, str):
                continue
            flag_counts["Champion Defeated"] += 1
    return flag_counts


def format_code(code: str) -> str:
    regexs = [
        (r'-', '_'),
        (r'[\s\\]', '_'),
        (r'\?\?\?', 'unknown'),
        (r'[\(\)]', ''),
        (r'^([0-9])', r'_\g<0>'),
        (r'\'', ''),
    ]
    for regex in regexs:
        code = re.sub(*regex, code)
    return (code.lower().replace(' ', '_')
            .replace('\'', '_')
            .replace('???', 'unknown')
            .replace('(', '')
            .replace(')', ''))


def combine_access(current, to_add, op):
    # print('combine_access', current, to_add, op)
    new = current.copy()
    if op == "AND":
        if len(current) == 0:
            return to_add
        i = 0
        for v2 in current:
            for v in to_add:
                if i >= len(new):
                    new.append([])
                new[i] = v2 + v
                i += 1
    if op == "OR":
        if len(current) == 0:
            return to_add
        if len(to_add) == 0:
            return current
        for v in to_add:
            new.append(v)
    # print('combine_access', 'result', new)
    return new
