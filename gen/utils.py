import json


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


def format_code(code: str):
    return code.lower().replace(' ', '_').replace('\'', '_').replace('???', 'unknown')
