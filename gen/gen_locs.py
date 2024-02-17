import enum
import json
from typing import Optional

from PyPopTracker.packs.locations import PopTrackerLocation, PopTrackerSection, PopTrackerMapLocation, export_locations


class CheckType(enum.IntEnum):
    CHEST = 0
    GIFT = 1
    ENCOUNTER = 2
    CHAMPION = 3
    FLAG = 4


MAIN_MAP_NAME = 'overview'
TILE_SIZE = 24
loc_by_name: dict[str, PopTrackerLocation | PopTrackerSection] = {}

with open('data/location_names.json', mode='r') as f:
    loc_names = json.load(f)

map_location_mapping = {
    0: ['MountainPath_North3_6'],
    1: ['MountainPath_North3_5'],
    2: ['MountainPath_North3_4'],
    3: ['MountainPath_North3_3'],
    4: ['MountainPath_North5_9'],
    5: ['MountainPath_North5_8'],
    6: ['MountainPath_North5_6'],
    7: ['MountainPath_Center1_5'],
    8: ['MountainPath_Center2_4', 'MountainPath_Center2_3'],
    9: ['MountainPath_Center3_6', 'MountainPath_Center3_8', 'MountainPath_Center3_9'],
    10: ['MountainPath_Center3_7'],
    11: ['MountainPath_Center4_0', 'MountainPath_Center4_4'],
    12: ['MountainPath_Center5_6'],
    13: ['MountainPath_Center5_13'],
    14: ['MountainPath_West1_4'],
    15: ['MountainPath_West2_22'],
    16: ['MountainPath_West2_19'],
    17: ['MountainPath_WestHidden_0'],
    18: ['MountainPath_WestHidden2_1'],
    19: ['MountainPath_North6_1', 'MountainPath_North6_2'],
    20: ['MountainPath_North7_1'],
    21: ['MountainPath_West4_1'],
    22: ['MountainPath_West4_3'],
    23: ['MountainPath_West4_6'],
    24: ['MountainPath_West6_134', 'MountainPath_West6_135', 'MountainPath_West6_136',
         'MountainPath_West6_2100040', 'MountainPath_West6_Champion'],
    25: ['MountainPath_SnowyEntrance2_14'],
    26: ['MountainPath_Center6_Lower_5'],
    27: ['MountainPath_Center6_Lower_2', 'MountainPath_Center6_Lower_10'],
    28: ['MountainPath_Center6_Upper_6'],
    29: ['MountainPath_Center7_3'],
    30: ['MountainPath_Center7_Champion'],
    31: ['BlueCave_NorthFork_Lower_4', 'BlueCave_NorthFork_Upper_10'],
    32: ['BlueCave_NorthFork_Lower_7'],
    33: ['BlueCave_NorthFork_Lower_12'],
    34: ['BlueCave_Chains2_3', 'BlueCave_Chains2_4'],
    35: ['BlueCave_NorthFork_West_11'],
    36: ['BlueCave_WestStairwell2_5'],
    37: ['BlueCave_Platforms_1', 'BlueCave_Platforms_0'],
    38: ['BlueCave_Platforms_3'],
    39: ['KeeperStronghold_Storage_5', 'KeeperStronghold_Storage_6'],
    40: ['KeeperStronghold_Smith_290', 'KeeperStronghold_Smith_291', 'KeeperStronghold_Smith_292',
         'KeeperStronghold_Smith_293', 'KeeperStronghold_Smith_294'],
    41: ['KeeperStronghold_WestStairwell_5'],
    42: ['KeeperStronghold_WestTowers_4'],
    43: ['KeeperStronghold_ParentsRoom_403', 'KeeperStronghold_ParentsRoom_326',
         'KeeperStronghold_ParentsRoom_2800011', 'KeeperStronghold_ParentsRoom_2800021',
         'KeeperStronghold_ParentsRoom_2800022', 'KeeperStronghold_ParentsRoom_2800023',
         'KeeperStronghold_ParentsRoom_2800024'],
    44: ['BlueCave_West2_4'],
    45: ['BlueCave_WestHidden_1'],
    46: ['BlueCave_West1_0'],
    47: ['BlueCave_West1_1'],
    48: ['BlueCave_CentralPart_7'],
    49: ['BlueCave_CentralPart_9', 'BlueCave_CentralPart_6'],
    50: ['BlueCave_East4_0', 'BlueCave_East4_1'],
    51: ['BlueCave_East3_0', 'BlueCave_East3_1'],
    52: ['BlueCave_WestWaters2_Lower_4'],
    53: ['BlueCave_WestWaters2_Lower_5'],
    54: ['BlueCave_WestWatersHidden_0', 'BlueCave_WestWatersHidden_1'],
    55: ['BlueCave_WestWaters7_East_10500008'],
    56: ['BlueCave_WestWaters7_West_2', 'BlueCave_WestWaters7_East_6'],
    57: ['BlueCave_ChampionRoom2_3', 'BlueCave_ChampionRoom2_Champion'],
    58: ['BlueCave_WestWaters5_0'],
    59: ['BlueCave_WestWatersHidden2_0', 'BlueCave_WestWatersHidden2_2'],
    60: ['BlueCave_AquaEntrance_Lower_1'],
    61: ['BlueCave_AquaEntrance_Lower_3'],
    62: ['SunPalace_East1_Center_7', 'SunPalace_East1_Center_8', 'SunPalace_East1_Center_9'],
    63: ['SunPalace_EastChampion_Champion'],
    64: ['SunPalace_East2_2'],
    65: ['SunPalace_East3_5'],
    66: ['SunPalace_East3_6'],
    67: ['SunPalace_East4_4'],
    68: ['SunPalace_South3_5', 'SunPalace_South3_6'],
    69: ['SunPalace_South1_Upper_13', 'SunPalace_South1_Lower_5'],
    70: ['SunPalace_South1_Lower_6'],
    71: ['SunPalace_South1_Lower_7', 'SunPalace_South1_Lower_8'],
    72: ['SunPalace_EastSewers2_6'],
    73: ['SunPalace_EastSewers4_4'],
    74: ['SunPalace_East6_Champion'],
    75: ['SunPalace_WestSewers1_4'],
    76: ['SunPalace_WestSewers4_5', 'SunPalace_WestSewers4_4'],
    77: ['SunPalace_WestSewersSecret_1', 'SunPalace_WestSewersSecret_2'],
    78: ['SunPalace_WestSewersSecret2_0'],
    79: ['SunPalace_West4_0'],
    80: ['SunPalace_West4_4'],
    81: ['SunPalace_West4_2'],
    82: ['SunPalace_West2_4'],
    83: ['SunPalace_West1_5'],
    84: ['SunPalace_West1_3'],
    85: ['SunPalace_West3_2'],
    86: ['SunPalace_West3_19700006'],
    87: ['StrongholdDungeon_Jail_5'],
    88: ['StrongholdDungeon_Jail_7'],
    89: ['StrongholdDungeon_North2_17'],
    90: ['StrongholdDungeon_North6_18'],
    91: ['StrongholdDungeon_NorthHidden_0'],
    92: ['StrongholdDungeon_West1_5', 'StrongholdDungeon_West1_12'],
    93: ['StrongholdDungeon_West4_Hidden_15'],
    94: ['StrongholdDungeon_Central1_19'],
    95: ['StrongholdDungeon_Hidden1_8', 'StrongholdDungeon_Hidden1_10',
         'StrongholdDungeon_Hidden1_11'],
    96: ['StrongholdDungeon_North5_3'],
    97: ['AncientWoods_West1_4'],
    98: ['AncientWoods_WestJumpPuzzle_46'],
    99: ['AncientWoods_WestHidden_2'],
    100: ['AncientWoods_West4_2'],
    101: ['AncientWoods_West5_1'],
    102: ['AncientWoods_Center1_1'],
    103: ['AncientWoods_Center1_0'],
    104: ['BlueCave_ChampionRoom3_Champion'],
    105: ['BlueCave_South1_Lower_5'],
    106: ['BlueCave_South3_1'],
    107: ['BlueCave_South3_2'],
    108: ['BlueCave_South2_0'],
    109: ['BlueCave_South6_4'],
    110: ['BlueCave_South4_4'],
    111: ['BlueCave_CentralPart_9', 'BlueCave_CentralPart_6'],
    112: ['SunPalace_North2_20800142', 'SunPalace_North2_20800117', 'SunPalace_North2_20800135'],
    113: ['SunPalace_Center_13'],
    114: ['SnowyPeaks_SunPalaceEntrance_5'],
    115: ['SnowyPeaks_WestDark_3'],
    116: ['SnowyPeaks_West2_1'],
    117: ['SnowyPeaks_West3_7'],
    118: ['SnowyPeaks_West3_4'],
    119: ['SnowyPeaks_West3_5'],
    120: ['SnowyPeaks_West4_7'],
    121: ['SnowyPeaks_West5_4'],
    122: ['SnowyPeaks_West5_5'],
    123: ['SnowyPeaks_ChampionRoom2_Champion'],
    124: ['SnowyPeaks_ChampionRoom_Champion', 'SnowyPeaks_ChampionRoom_17000045',
          'SnowyPeaks_ChampionRoom_11'],
    125: ['SnowyPeaks_Lake_West_12', 'SnowyPeaks_Lake_West_10'],
    126: ['SnowyPeaks_Lake_Lower_9'],
    127: ['SnowyPeaks_WestMountain2_4'],
    128: ['SnowyPeaks_WestMountain3_7'],
    129: ['SnowyPeaks_WestMountain3_8'],
    130: ['SnowyPeaks_WestMountain6_5'],
    131: ['SnowyPeaks_WestMountain7_6'],
    132: ['SnowyPeaks_WestMountain7_7'],
    133: ['SnowyPeaks_WestMountainSecret_2'],
    134: ['SnowyPeaks_WestMountain7_8'],
    135: ['SnowyPeaks_EastMountain1_9'],
    136: ['SnowyPeaks_EastMountain1_10'],
    137: ['SnowyPeaks_EastMountainTop_0'],
    138: ['SnowyPeaks_ClothesmakerHouse_17700033'],
    139: ['SnowyPeaks_EastMountain4_5'],
    140: ['SnowyPeaks_EastMountain5_9'],
    141: ['SnowyPeaks_EastMountain5_10'],
    142: ['SnowyPeaks_EastMountain3_Upper_24'],
    143: ['SnowyPeaks_EastMountain3_Middle_15'],
    144: ['SnowyPeaks_EastMountain3_Lower_16'],
    145: ['SnowyPeaks_HighChallenge_11'],
    146: ['SnowyPeaks_HighChallenge_12'],
    147: ['SnowyPeaks_EastMountain2_23'],
    148: ['SnowyPeaks_EastMountain2_21'],
    149: ['SnowyPeaks_EastMountain2_22'],
    150: ['SnowyPeaks_EastDark_8', 'SnowyPeaks_EastDark_9'],
    151: ['SnowyPeaks_East4_Middle_9'],
    152: ['SnowyPeaks_East4_Lower_5'],
    153: ['SnowyPeaks_East5_17'],
    154: ['SnowyPeaks_East3_9', 'SnowyPeaks_East3_8'],
    155: ['SnowyPeaks_East3_10'],
    156: ['SnowyPeaks_East2_Upper_3'],
    157: ['SnowyPeaks_East2_Lower_4'],
    158: ['SnowyPeaks_East2_Upper_7'],
    159: ['StrongholdDungeon_Central3_15'],
    160: ['StrongholdDungeon_Central3_0'],
    161: ['StrongholdDungeon_Central4_12100029', 'StrongholdDungeon_Central4_12100041'],
    162: ['StrongholdDungeon_Hidden1_12'],
    163: ['StrongholdDungeon_SummonRoom_Champion'],
    164: ['StrongholdDungeon_South1_5'],
    165: ['StrongholdDungeon_South2_Champion'],
    166: ['StrongholdDungeon_West3_9'],
    167: ['StrongholdDungeon_South4_6'],
    168: ['StrongholdDungeon_Library_14200159'],
    169: ['StrongholdDungeon_Library2_1', 'StrongholdDungeon_Library2_2'],
    170: ['StrongholdDungeon_East1_SW_6'],
    171: ['StrongholdDungeon_East1_NE_7'],
    172: ['StrongholdDungeon_East1_SE_9'],
    173: ['StrongholdDungeon_EastKeys_0', 'StrongholdDungeon_EastKeys_1'],
    174: ['StrongholdDungeon_EastHidden_0'],
    175: ['StrongholdDungeon_East3_11'],
    176: ['StrongholdDungeon_East5_10'],
    177: ['MagmaChamber_West1_East_41'],
    178: ['MagmaChamber_West6_Lower_1'],
    179: ['MagmaChamber_West2_4'],
    180: ['MagmaChamber_West4_Ledge_3'],
    181: ['MagmaChamber_West4_Upper_0'],
    182: ['MagmaChamber_North2_0', 'MagmaChamber_North2_1'],
    183: ['MagmaChamber_North1_5'],
    184: ['MagmaChamber_North3_4'],
    185: ['MagmaChamber_North5_Upper_3'],
    186: ['MagmaChamber_East2_3'],
    187: ['MagmaChamber_East1_3'],
    188: ['AncientWoods_West6_7'],
    189: ['AncientWoods_West6_6'],
    190: ['AncientWoods_WestHidden2_0'],
    191: ['AncientWoods_WestDescent_Upper_12'],
    192: ['AncientWoods_SouthHidden1_West_3'],
    193: ['AncientWoods_SouthHidden1_East_8'],
    194: ['AncientWoods_SouthHidden3_2'],
    195: ['AncientWoods_SouthChampion_Champion'],
    196: ['AncientWoods_WestDescent3_12'],
    197: ['AncientWoods_DarkRoom2_2'],
    198: ['StrongholdDungeon_Central5_Upper_7'],
    199: ['StrongholdDungeon_North4_2'],
    200: ['MysticalWorkshop_South6_0'],
    201: ['MysticalWorkshop_South5_5', 'MysticalWorkshop_South5_7'],
    202: ['MysticalWorkshop_South4_19', 'MysticalWorkshop_South4_18'],
    203: ['MysticalWorkshop_Center6_3'],
    204: ['MysticalWorkshop_West3_Access_0'],
    205: ['MysticalWorkshop_Center4_1'],
    206: ['MysticalWorkshop_Center5_Upper_3'],
    207: ['MysticalWorkshop_Center5_Middle_6'],
    208: ['MysticalWorkshop_Center5_Lower_5'],
    209: ['MysticalWorkshop_Center9_0'],
    210: ['MysticalWorkshop_Center8_6'],
    211: ['MysticalWorkshop_West2_8', 'MysticalWorkshop_West2_9'],
    212: ['MysticalWorkshop_Center7_1'],
    213: ['MysticalWorkshop_Center7_0'],
    214: ['MysticalWorkshop_Center3_0'],
    215: ['MysticalWorkshop_Center3_1'],
    216: ['MysticalWorkshop_East1_9'],
    217: ['MysticalWorkshop_East3_3'],
    218: ['MysticalWorkshop_East2_1'],
    219: ['MysticalWorkshop_North2_1'],
    220: ['MysticalWorkshop_North4_Shortcut_9'],
    221: ['MysticalWorkshop_North1_1'],
    222: ['MysticalWorkshop_North1_0'],
    223: ['MysticalWorkshop_North3_5'],
    224: ['MysticalWorkshop_North6_0'],
    225: ['MysticalWorkshop_North4_Upper_8'],
    226: ['MysticalWorkshop_Hidden_0', 'MysticalWorkshop_Hidden_1', 'MysticalWorkshop_Hidden_3'],
    227: ['MysticalWorkshop_North4_Upper_Champion'],
    228: ['AncientWoods_DoorPuzzle_13'],
    229: ['AncientWoods_DoorPuzzle_14', 'AncientWoods_DoorPuzzle_15'],
    230: ['MountainPath_NorthHidden_4'],
    231: ['KeeperStronghold_DuelCircle_701'],
    232: ['MagmaChamber_North7_4'],
    233: ['MagmaChamber_Center2_Lower_16'],
    234: ['MagmaChamber_Center2_Middle_9'],
    235: ['MagmaChamber_Center3_1'],
    236: ['MagmaChamber_Center4_West_0'],
    237: ['MagmaChamber_Center4_East_3'],
    238: ['MagmaChamber_Center5_0'],
    239: ['MagmaChamber_CenterMagmaRoom_1', 'MagmaChamber_CenterMagmaRoom_6'],
    240: ['MagmaChamber_South2_1'],
    241: ['MagmaChamber_Center6_Lower_12'],
    242: ['MagmaChamber_Center7_1'],
    243: ['MagmaChamber_AlchemistLab_East_27700082'],
    244: ['MagmaChamber_Center9_Middle_12'],
    245: ['MagmaChamber_Center10_6']
}

for k, v in map_location_mapping.items():
    map_location_mapping[k] = [loc_names[v2] for v2 in v]

map_locations = {
    0: [(MAIN_MAP_NAME, 895, 702)],
    1: [(MAIN_MAP_NAME, 895 + TILE_SIZE, 702)],
    2: [(MAIN_MAP_NAME, 895, 702 - TILE_SIZE)],
    3: [(MAIN_MAP_NAME, 895 + 24, 702 - TILE_SIZE)],
    4: [(MAIN_MAP_NAME, 990, 678)],
    5: [(MAIN_MAP_NAME, 990, 678 + TILE_SIZE * 2)],
    6: [(MAIN_MAP_NAME, 990, 678 + TILE_SIZE * 3)],
    7: [(MAIN_MAP_NAME, 918, 727)],
    8: [(MAIN_MAP_NAME, 843, 727)],
    9: [(MAIN_MAP_NAME, 773, 775)],
    10: [(MAIN_MAP_NAME, 773, 775 - TILE_SIZE)],
    11: [(MAIN_MAP_NAME, 849, 775)],
    12: [(MAIN_MAP_NAME, 728, 726)],
    13: [(MAIN_MAP_NAME, 728 + TILE_SIZE, 726 + TILE_SIZE)],
    14: [(MAIN_MAP_NAME, 680, 748)],
    15: [(MAIN_MAP_NAME, 632, 702)],
    16: [(MAIN_MAP_NAME, 632, 800)],
    17: [(MAIN_MAP_NAME, 606, 800)],
    18: [(MAIN_MAP_NAME, 583, 775)],
    19: [(MAIN_MAP_NAME, 728, 702)],
    20: [(MAIN_MAP_NAME, 728 + TILE_SIZE, 702)],
    21: [(MAIN_MAP_NAME, 606, 702)],
    22: [(MAIN_MAP_NAME, 606, 702 + TILE_SIZE)],
    23: [(MAIN_MAP_NAME, 606 - TILE_SIZE, 702)],
    24: [(MAIN_MAP_NAME, 532, 726)],
    25: [(MAIN_MAP_NAME, 560, 750)],
    26: [(MAIN_MAP_NAME, 704, 798)],
    27: [(MAIN_MAP_NAME, 704, 798 + TILE_SIZE)],
    28: [(MAIN_MAP_NAME, 704, 798 - TILE_SIZE)],
    29: [(MAIN_MAP_NAME, 728, 775)],
    30: [(MAIN_MAP_NAME, 728 + TILE_SIZE, 775)],
    31: [(MAIN_MAP_NAME, 1012, 748)],
    32: [(MAIN_MAP_NAME, 1012 + TILE_SIZE, 748)],
    33: [(MAIN_MAP_NAME, 1012 + TILE_SIZE, 748 + TILE_SIZE * 2)],
    34: [(MAIN_MAP_NAME, 1012 - TILE_SIZE, 748 + TILE_SIZE)],
    35: [(MAIN_MAP_NAME, 1012, 748 + TILE_SIZE)],
    36: [(MAIN_MAP_NAME, 918, 824)],
    37: [(MAIN_MAP_NAME, 1062, 798)],
    38: [(MAIN_MAP_NAME, 1062 + TILE_SIZE, 798)],
    39: [(MAIN_MAP_NAME, 1234, 748)],
    40: [(MAIN_MAP_NAME, 1160, 702)],
    41: [(MAIN_MAP_NAME, 1112, 678)],
    42: [(MAIN_MAP_NAME, 1062, 702)],
    43: [(MAIN_MAP_NAME, 1280, 702)],
    44: [(MAIN_MAP_NAME, 942, 869)],
    45: [(MAIN_MAP_NAME, 942 - TILE_SIZE, 869)],
    46: [(MAIN_MAP_NAME, 1012, 869)],
    47: [(MAIN_MAP_NAME, 1012 + TILE_SIZE, 869)],
    48: [(MAIN_MAP_NAME, 1086, 846)],
    49: [(MAIN_MAP_NAME, 1086 + TILE_SIZE, 846 - TILE_SIZE)],
    50: [(MAIN_MAP_NAME, 1156, 822)],
    51: [(MAIN_MAP_NAME, 1228, 846)],
    52: [(MAIN_MAP_NAME, 870, 846)],
    53: [(MAIN_MAP_NAME, 870 + TILE_SIZE, 846)],
    54: [(MAIN_MAP_NAME, 870, 846 + TILE_SIZE)],
    55: [(MAIN_MAP_NAME, 774, 798)],
    56: [(MAIN_MAP_NAME, 774 - TILE_SIZE, 798)],
    57: [(MAIN_MAP_NAME, 774 - TILE_SIZE * 2, 798)],
    58: [(MAIN_MAP_NAME, 848, 846)],
    59: [(MAIN_MAP_NAME, 800, 870)],
    60: [(MAIN_MAP_NAME, 728, 894)],
    61: [(MAIN_MAP_NAME, 728 + TILE_SIZE, 894)],
    62: [(MAIN_MAP_NAME, 728 - TILE_SIZE, 894 - TILE_SIZE)],
    63: [(MAIN_MAP_NAME, 608, 846)],
    64: [(MAIN_MAP_NAME, 656, 896)],
    65: [(MAIN_MAP_NAME, 608, 918)],
    66: [(MAIN_MAP_NAME, 608 - TILE_SIZE, 918)],
    67: [(MAIN_MAP_NAME, 514, 918)],
    68: [(MAIN_MAP_NAME, 536, 968)],
    69: [(MAIN_MAP_NAME, 488, 968)],
    70: [(MAIN_MAP_NAME, 488 - TILE_SIZE, 968 + TILE_SIZE)],
    71: [(MAIN_MAP_NAME, 488, 968 + TILE_SIZE * 2)],
    72: [(MAIN_MAP_NAME, 560, 1018)],
    73: [(MAIN_MAP_NAME, 656, 966)],
    74: [(MAIN_MAP_NAME, 632, 918)],
    75: [(MAIN_MAP_NAME, 414, 1018)],
    76: [(MAIN_MAP_NAME, 342, 1018)],
    77: [(MAIN_MAP_NAME, 392, 966)],
    78: [(MAIN_MAP_NAME, 342, 966)],
    79: [(MAIN_MAP_NAME, 296, 942)],
    80: [(MAIN_MAP_NAME, 296 + TILE_SIZE, 942)],
    81: [(MAIN_MAP_NAME, 296 + TILE_SIZE * 2, 942 - TILE_SIZE)],
    82: [(MAIN_MAP_NAME, 368, 846)],
    83: [(MAIN_MAP_NAME, 296, 846)],
    84: [(MAIN_MAP_NAME, 296, 846 - TILE_SIZE)],
    85: [(MAIN_MAP_NAME, 392, 918)],
    86: [(MAIN_MAP_NAME, 392 + TILE_SIZE, 918 - TILE_SIZE)],
    87: [(MAIN_MAP_NAME, 1254, 752)],
    88: [(MAIN_MAP_NAME, 1254, 752 + TILE_SIZE)],
    89: [(MAIN_MAP_NAME, 1352, 752)],
    90: [(MAIN_MAP_NAME, 1328, 774)],
    91: [(MAIN_MAP_NAME, 1328 - TILE_SIZE, 774)],
    92: [(MAIN_MAP_NAME, 1280, 798)],
    93: [(MAIN_MAP_NAME, 1228, 822)],
    94: [(MAIN_MAP_NAME, 1400, 774)],
    95: [(MAIN_MAP_NAME, 1426, 872)],
    96: [(MAIN_MAP_NAME, 1448, 728)],
    97: [(MAIN_MAP_NAME, 1592, 728)],
    98: [(MAIN_MAP_NAME, 1496 + TILE_SIZE, 752)],
    99: [(MAIN_MAP_NAME, 1496, 752)],
    100: [(MAIN_MAP_NAME, 1616, 752)],
    101: [(MAIN_MAP_NAME, 1664, 752)],
    102: [(MAIN_MAP_NAME, 1762, 728)],
    103: [(MAIN_MAP_NAME, 1762 - TILE_SIZE, 728 + TILE_SIZE)],
    104: [(MAIN_MAP_NAME, 1208, 895)],
    105: [(MAIN_MAP_NAME, 1136, 920)],
    106: [(MAIN_MAP_NAME, 1113, 895)],
    107: [(MAIN_MAP_NAME, 1113 - TILE_SIZE, 895)],
    108: [(MAIN_MAP_NAME, 1208, 920)],
    109: [(MAIN_MAP_NAME, 1136, 920 + TILE_SIZE)],
    110: [(MAIN_MAP_NAME, 1136 + TILE_SIZE, 920 + TILE_SIZE * 2)],
    111: [(MAIN_MAP_NAME, 1400 + TILE_SIZE, 774 - TILE_SIZE)],
    112: [(MAIN_MAP_NAME, 464, 798)],
    113: [(MAIN_MAP_NAME, 464, 872)],
    114: [(MAIN_MAP_NAME, 274, 752)],
    115: [(MAIN_MAP_NAME, 176, 728)],
    116: [(MAIN_MAP_NAME, 202, 678)],
    117: [(MAIN_MAP_NAME, 128, 678)],
    118: [(MAIN_MAP_NAME, 128, 678 + TILE_SIZE)],
    119: [(MAIN_MAP_NAME, 128 + TILE_SIZE, 678 + TILE_SIZE)],
    120: [(MAIN_MAP_NAME, 106, 654)],
    121: [(MAIN_MAP_NAME, 80, 678)],
    122: [(MAIN_MAP_NAME, 80, 678 - TILE_SIZE)],
    123: [(MAIN_MAP_NAME, 106, 678 - TILE_SIZE * 2)],
    124: [(MAIN_MAP_NAME, 128, 728)],
    125: [(MAIN_MAP_NAME, 32, 702)],
    126: [(MAIN_MAP_NAME, 32, 702 + TILE_SIZE)],
    127: [(MAIN_MAP_NAME, 102, 606)],
    128: [(MAIN_MAP_NAME, 152, 606)],
    129: [(MAIN_MAP_NAME, 152, 606 - TILE_SIZE)],
    130: [(MAIN_MAP_NAME, 152 + TILE_SIZE, 606)],
    131: [(MAIN_MAP_NAME, 152, 534)],
    132: [(MAIN_MAP_NAME, 152, 534 - TILE_SIZE)],
    133: [(MAIN_MAP_NAME, 152 + TILE_SIZE, 534 - TILE_SIZE)],
    134: [(MAIN_MAP_NAME, 152 - TILE_SIZE, 534 - TILE_SIZE * 2)],
    135: [(MAIN_MAP_NAME, 366, 532)],
    136: [(MAIN_MAP_NAME, 366 + TILE_SIZE, 532)],
    137: [(MAIN_MAP_NAME, 366 + TILE_SIZE * 2, 532)],
    138: [(MAIN_MAP_NAME, 440, 560)],
    139: [(MAIN_MAP_NAME, 392, 582)],
    140: [(MAIN_MAP_NAME, 440, 560 + TILE_SIZE)],
    141: [(MAIN_MAP_NAME, 440, 560 + TILE_SIZE * 2)],
    142: [(MAIN_MAP_NAME, 465, 630)],
    143: [(MAIN_MAP_NAME, 465, 630 + TILE_SIZE)],
    144: [(MAIN_MAP_NAME, 465 - TILE_SIZE, 630 + TILE_SIZE * 2)],
    145: [(MAIN_MAP_NAME, 416, 606)],
    146: [(MAIN_MAP_NAME, 416, 606 + TILE_SIZE)],
    147: [(MAIN_MAP_NAME, 392, 606)],
    148: [(MAIN_MAP_NAME, 392, 606 + TILE_SIZE)],
    149: [(MAIN_MAP_NAME, 392, 606 + TILE_SIZE * 2)],
    150: [(MAIN_MAP_NAME, 392, 606 + TILE_SIZE * 3)],
    151: [(MAIN_MAP_NAME, 368, 702)],
    152: [(MAIN_MAP_NAME, 368 - TILE_SIZE, 702 + TILE_SIZE)],
    153: [(MAIN_MAP_NAME, 272, 702)],
    154: [(MAIN_MAP_NAME, 392, 750)],
    155: [(MAIN_MAP_NAME, 392 + TILE_SIZE * 2, 750 - TILE_SIZE)],
    156: [(MAIN_MAP_NAME, 462, 750 - TILE_SIZE)],
    157: [(MAIN_MAP_NAME, 462 + TILE_SIZE, 750 - TILE_SIZE)],
    158: [(MAIN_MAP_NAME, 462, 750)],
    159: [(MAIN_MAP_NAME, 1448, 798)],
    160: [(MAIN_MAP_NAME, 1448, 798 + TILE_SIZE)],
    161: [(MAIN_MAP_NAME, 1472, 872)],
    162: [(MAIN_MAP_NAME, 1400, 872)],
    163: [(MAIN_MAP_NAME, 1400 - TILE_SIZE, 872)],
    164: [(MAIN_MAP_NAME, 1372, 944)],
    165: [(MAIN_MAP_NAME, 1328, 920)],
    166: [(MAIN_MAP_NAME, 1280, 846)],
    167: [(MAIN_MAP_NAME, 1280, 920)],
    168: [(MAIN_MAP_NAME, 1376, 968)],
    169: [(MAIN_MAP_NAME, 1376 + TILE_SIZE, 968)],
    170: [(MAIN_MAP_NAME, 1472, 942)],
    171: [(MAIN_MAP_NAME, 1472 + TILE_SIZE, 942 - TILE_SIZE)],
    172: [(MAIN_MAP_NAME, 1472 + TILE_SIZE, 942)],
    173: [(MAIN_MAP_NAME, 1520, 990)],
    174: [(MAIN_MAP_NAME, 1520 - TILE_SIZE, 990 - TILE_SIZE)],
    175: [(MAIN_MAP_NAME, 1568, 942)],
    176: [(MAIN_MAP_NAME, 1542, 920)],
    177: [(MAIN_MAP_NAME, 1690, 968)],
    178: [(MAIN_MAP_NAME, 1712, 1040)],
    179: [(MAIN_MAP_NAME, 1690 + 2 * TILE_SIZE, 968)],
    180: [(MAIN_MAP_NAME, 1810, 942)],
    181: [(MAIN_MAP_NAME, 1810, 942 - TILE_SIZE)],
    182: [(MAIN_MAP_NAME, 1880, 872)],
    183: [(MAIN_MAP_NAME, 1924, 894)],
    184: [(MAIN_MAP_NAME, 1976, 872)],
    185: [(MAIN_MAP_NAME, 2000, 846)],
    186: [(MAIN_MAP_NAME, 2144, 870)],
    187: [(MAIN_MAP_NAME, 2120, 894)],
    188: [(MAIN_MAP_NAME, 1638, 800)],
    189: [(MAIN_MAP_NAME, 1638 + TILE_SIZE, 800 + TILE_SIZE)],
    190: [(MAIN_MAP_NAME, 1638 + TILE_SIZE * 2, 800 + TILE_SIZE)],
    191: [(MAIN_MAP_NAME, 1638 - TILE_SIZE * 2, 800)],
    192: [(MAIN_MAP_NAME, 1618, 846)],
    193: [(MAIN_MAP_NAME, 1618 + TILE_SIZE * 2, 846)],
    194: [(MAIN_MAP_NAME, 1760, 800)],
    195: [(MAIN_MAP_NAME, 1760 + TILE_SIZE * 2, 800)],
    196: [(MAIN_MAP_NAME, 1568, 872)],
    197: [(MAIN_MAP_NAME, 1592, 896)],
    198: [(MAIN_MAP_NAME, 1496, 872)],
    199: [(MAIN_MAP_NAME, 1424, 702)],
    200: [(MAIN_MAP_NAME, 1424 + 2 * TILE_SIZE, 702)],
    201: [(MAIN_MAP_NAME, 1400, 702)],
    202: [(MAIN_MAP_NAME, 1400 - 2 * TILE_SIZE, 702)],
    203: [(MAIN_MAP_NAME, 1496, 678)],
    204: [(MAIN_MAP_NAME, 1424, 630)],
    205: [(MAIN_MAP_NAME, 1496, 606)],
    206: [(MAIN_MAP_NAME, 1448, 558)],
    207: [(MAIN_MAP_NAME, 1448 + TILE_SIZE, 558 + TILE_SIZE)],
    208: [(MAIN_MAP_NAME, 1448, 558 + 2 * TILE_SIZE)],
    209: [(MAIN_MAP_NAME, 1448 + TILE_SIZE * 2, 558 + TILE_SIZE)],
    210: [(MAIN_MAP_NAME, 1448 - TILE_SIZE, 558 - TILE_SIZE)],
    211: [(MAIN_MAP_NAME, 1448 - TILE_SIZE, 558 + 2 * TILE_SIZE)],
    212: [(MAIN_MAP_NAME, 1448 + 2 * TILE_SIZE, 558)],
    213: [(MAIN_MAP_NAME, 1448 + 2 * TILE_SIZE, 558 - TILE_SIZE)],
    214: [(MAIN_MAP_NAME, 1448, 558 - 2 * TILE_SIZE)],
    215: [(MAIN_MAP_NAME, 1448 + TILE_SIZE, 558 - 2 * TILE_SIZE)],
    216: [(MAIN_MAP_NAME, 1496, 486)],
    217: [(MAIN_MAP_NAME, 1496 + TILE_SIZE * 2, 486)],
    218: [(MAIN_MAP_NAME, 1496 + TILE_SIZE, 486 + TILE_SIZE * 2)],
    219: [(MAIN_MAP_NAME, 1496, 486 - TILE_SIZE)],
    220: [(MAIN_MAP_NAME, 1496 - TILE_SIZE, 486 - 2 * TILE_SIZE)],
    221: [(MAIN_MAP_NAME, 1448, 486)],
    222: [(MAIN_MAP_NAME, 1448 + TILE_SIZE, 486 - TILE_SIZE)],
    223: [(MAIN_MAP_NAME, 1396, 512)],
    224: [(MAIN_MAP_NAME, 1396, 512 - TILE_SIZE * 3)],
    225: [(MAIN_MAP_NAME, 1448, 416)],
    226: [(MAIN_MAP_NAME, 1448 - TILE_SIZE * 2, 416)],
    227: [(MAIN_MAP_NAME, 1448 + TILE_SIZE, 416)],
    228: [(MAIN_MAP_NAME, 1710, 800)],
    229: [(MAIN_MAP_NAME, 1710, 800+TILE_SIZE)],
    230: [(MAIN_MAP_NAME, 1016, 678)],
    231: [(MAIN_MAP_NAME, 1184, 654)],
    232: [(MAIN_MAP_NAME, 2046, 894)],
    233: [(MAIN_MAP_NAME, 1856, 1016)],
    234: [(MAIN_MAP_NAME, 1856 + TILE_SIZE, 1016 - TILE_SIZE)],
    235: [(MAIN_MAP_NAME, 1832, 968)],
    236: [(MAIN_MAP_NAME, 1832+TILE_SIZE*3, 968)],
    237: [(MAIN_MAP_NAME, 1832+TILE_SIZE*4, 968)],
    238: [(MAIN_MAP_NAME, 1904, 1040)],
    239: [(MAIN_MAP_NAME, 1904-TILE_SIZE*3, 1040)],
    240: [(MAIN_MAP_NAME, 2000, 1040)],
    241: [(MAIN_MAP_NAME, 2000-TILE_SIZE, 1040-TILE_SIZE*2)],
    242: [(MAIN_MAP_NAME, 2000-TILE_SIZE*2, 1040-TILE_SIZE*3)],
    243: [(MAIN_MAP_NAME, 2024, 968)],
    244: [(MAIN_MAP_NAME, 2096, 968-TILE_SIZE)],
    245: [(MAIN_MAP_NAME, 2120, 968+TILE_SIZE)],
}


def get_access(req_data: Optional[list], op: Optional[str] = "AND"):
    # print('get_access', req_data, op)
    if req_data is None:
        return []
    if isinstance(req_data, str):
        return [[f'${req_data}']]
    # ToDo
    result: list[list[str]] = []
    skip_next = False
    for i in range(0, len(req_data)):
        if skip_next:
            skip_next = False
            continue
        if req_data[i] == "OR" or req_data[i] == "AND":
            result = combine_access(result, get_access(req_data[i + 1], req_data[i]), op)
            skip_next = True
        else:
            if op == "AND":
                if 0 >= len(result):
                    result.append([])
                result[0].append(format_req(req_data[i]))
            if op == "OR":
                result.append([format_req(req_data[i])])
        # print('get_access', f'step {i}', result)
    return result


def format_req(req):
    if req.startswith('NOT '):
        return f'$_NOT_CALL|{req[4:]}'
    return f'${req}'


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
        for v in to_add:
            new.append(v)
    # print('combine_access', 'result', new)
    return new


def are_different_regions(loc_names, cur_region):
    for name in loc_names:
        if cur_region not in name:
            return True
    return False


def create_loc(locs: list[PopTrackerLocation], region: str, check_type_name, data, location_id,
               ids_for_sections, loc_names, count=1, clear_as_group=False):
    if check_type_name == "Rank":
        loc_name = loc_names[f'{region}_Champion']
    elif check_type_name == "Flag":
        loc_name = f"{check_type_name} {region}_{data['id']}"
    else:
        if region == 'Menu':
            loc_name = f'{check_type_name} {data["id"]}'
        else:
            loc_name = loc_names[f"{region}_{data['id']}"]
    # print('create_loc', region, loc_name, location_id)
    map_locs = None
    mapping_value = None
    multi_sec = False
    for k, v in map_location_mapping.items():
        if loc_name in v:
            map_locs = map_locations[k]
            mapping_value = v
            multi_sec = len(v) > 1
            break
    if map_locs is not None:
        map_locs = list(map(lambda x: PopTrackerMapLocation(*x), map_locs))
    access_rules = combine_access([[f"$has_access_to|{region}"]], get_access(data.get('requirements')), "AND")
    if multi_sec:
        parent_count = 1
        parent_region = region
        # if f'{region}_{data["id"]}' in subsections:
        #     parent_region = subsections[f'{region}_{data["id"]}']
        #     parent_region = parent_region[:parent_region.rfind("_")]
        temp_parent_name = parent_region
        parent_region = f'{temp_parent_name}'
        while True:
            loc = next((x for x in locs if x.name == parent_region), None)
            if loc is not None:
                first_sec = loc.sections[0]
                if first_sec.name not in mapping_value:
                    parent_count += 1
                    parent_region = f'{temp_parent_name} #{parent_count}'
                else:
                    break
            else:
                break
        if loc is None:
            loc = PopTrackerLocation(parent_region, map_locations=map_locs)
            locs.append(loc)
        sec = PopTrackerSection(loc_name, item_count=count, clear_as_group=clear_as_group, access_rules=access_rules)
        loc.sections.append(sec)
        loc_by_name[loc_name] = sec
        ids = []
        if location_id is not None:
            for i in range(0, count):
                ids.append(location_id)
                location_id += 1
            ids_for_sections[f'@{parent_region}/{loc_name}'] = ids
    else:
        loc = PopTrackerLocation(loc_name, map_locations=map_locs, access_rules=access_rules)
        loc.sections.append(PopTrackerSection("", item_count=count, clear_as_group=clear_as_group))
        loc_by_name[loc_name] = loc
        ids = []
        if location_id is not None:
            for i in range(0, count):
                ids.append(location_id)
                location_id += 1
            ids_for_sections[f'@{loc_name}/'] = ids
            for _id in ids:
                locs_by_id[_id] = loc_name
        locs.append(loc)
    return loc, location_id


def find_loc_with_same_map_loc(locs: list[PopTrackerLocation], map_locs: list[PopTrackerMapLocation]):
    for loc in locs:
        for map_loc in map_locs:
            if map_loc in loc.map_locations:
                return loc
    return None


def get_chest_loc(locs: list[PopTrackerLocation], region: str, data, location_id, ids_for_sections, loc_names):
    loc, location_id = create_loc(locs, region, 'Chest', data, location_id, ids_for_sections, loc_names)
    return loc, location_id


def get_gift_loc(locs: list[PopTrackerLocation], region: str, data, location_id, ids_for_sections, loc_names):
    loc, location_id = create_loc(locs, region, 'Gift', data, location_id, ids_for_sections, loc_names)
    return loc, location_id


def get_encounter_locs(locs: list[PopTrackerLocation], region: str, data, location_id, ids_for_sections, loc_names):
    loc, location_id = create_loc(locs, region, 'Encounter', data, location_id, ids_for_sections, loc_names, count=3,
                                  clear_as_group=True)
    return loc, location_id


def get_champ_locs(locs: list[PopTrackerLocation], region: str, data, location_id, ids_for_sections, subsections):
    loc, location_id = create_loc(locs, region, 'Rank', data, location_id, ids_for_sections, subsections)
    # loc, location_id = create_loc(locs, region, 'Champion', data, location_id, ids_for_sections, count=3,
    #                               clear_as_group=True)
    location_id += 3
    return loc, location_id


def get_flag_loc(locs: list[PopTrackerLocation], region: str, data, subsections):
    loc, _ = create_loc(locs, region, 'Flag', data, None, None, subsections)
    return loc, None



locs_by_id = {}


def gen_locations():
    with open('data/world.json', mode='r') as f:
        json_data = json.load(f)
    locs = []
    ids_for_sections = {}

    location_id = 970500
    for current_region_data in json_data:
        region_name = current_region_data['region']
        # region = PopTrackerLocation(region_name)

        # this is in regions.lua now
        # for conn_data in region_data.get("connections"):
        #     # Hack because we store comments as strings
        #     if isinstance(conn_data, str):
        #         continue

        for chest_data in current_region_data.get("chests") or []:
            # Hack because we store comments as strings
            if isinstance(chest_data, str):
                continue
            location, location_id = get_chest_loc(locs, region_name, chest_data, location_id, ids_for_sections,
                                                  loc_names)

        for gift_data in current_region_data.get("gifts") or []:
            # Hack because we store comments as strings
            if isinstance(gift_data, str):
                continue
            location, location_id = get_gift_loc(locs, region_name, gift_data, location_id, ids_for_sections,
                                                 loc_names)

        for encounter_data in current_region_data.get("encounters") or []:
            # Hack because we store comments as strings
            if isinstance(encounter_data, str):
                continue
            # location, location_id = get_encounter_locs(locs, region_name, encounter_data, location_id, ids_for_sections,
            #                                            loc_names)

        for champion_data in current_region_data.get("champion") or []:
            # Hack because we store comments as strings
            if isinstance(champion_data, str):
                continue
            location, location_id = get_champ_locs(locs, region_name, champion_data, location_id, ids_for_sections,
                                                   loc_names)

        for flag_data in current_region_data.get("flags") or []:
            # Hack because we store comments as strings
            if isinstance(flag_data, str):
                continue
            location, _ = get_flag_loc(locs, region_name, flag_data, loc_names)

        # locs.append(region)
    with open('data/plotless.json', mode='r') as f:
        json_data = json.load(f)
    for plotless_data in json_data:
        loc_type = plotless_data['type']
        if loc_type == 'connection':
            continue # handled by logic
        region_name = plotless_data['region']
        if loc_type == 'location':
            loc_type = 'Gift'  # ToDo: determine by id range
            loc_id = plotless_data['object_id']
        else:
            continue # ToDo?
        loc_name = loc_names[f'{region_name}_{loc_id}']
        loc = loc_by_name[loc_name]
        loc.access_rules = combine_access(loc.access_rules,
                                          combine_access(
                                              [[f'$has_access_to|{region_name}', '$plotless']],
                                              get_access(plotless_data['requirements']), 'AND')
                                          , 'OR')

    export_locations(locs, out_path='../locations/locations.json')
    print('Exported locations!')
    export_loction_mapping(ids_for_sections)
    print('Exported location mapping!')
    mapped_locs = []
    missing_locs = {}
    for k, v in map_location_mapping.items():
        mapped_locs += v
    for k, v in locs_by_id.items():
        if v not in mapped_locs:
            missing_locs[k] = v
    print(len(missing_locs), missing_locs)


def export_loction_mapping(ids_for_items: dict[str, list[int]]):
    lines = ['LOCATION_MAPPING = {']
    for k, v in ids_for_items.items():
        for i in v:
            lines.append(f'\t[{i}] = {{"{k}"}},')
    lines.append('}')

    with open('../scripts/autotracking/location_mapping.lua', mode='w') as f:
        f.write('\n'.join(lines))


if __name__ == "__main__":
    gen_locations()
