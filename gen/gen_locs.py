import enum
import json
import re
from os.path import commonprefix
from typing import Optional, Tuple, List, Any

from PyPopTracker.packs.locations import PopTrackerLocation, PopTrackerSection, PopTrackerMapLocation, export_locations


class CheckType(enum.IntEnum):
    CHEST = 0
    GIFT = 1
    ENCOUNTER = 2
    CHAMPION = 3
    FLAG = 4


MAIN_MAP_NAME = 'overview'
TILE_SIZE = 36
SUB_MAP_OFFSET = 32
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
    21: ['MountainPath_West4_3'],
    22: ['MountainPath_West4_1'],
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
    131: ['SnowyPeaks_WestMountain7_7'],
    132: ['SnowyPeaks_WestMountain7_6'],
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
    157: ['SnowyPeaks_East2_Upper_7'],
    158: ['SnowyPeaks_East2_Lower_4'],
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
    245: ['MagmaChamber_Center10_6'],
    246: ['AncientWoods_West3_0'],
    247: ['AncientWoods_TreeOfEvolution_7'],
    248: ['AncientWoods_TreeOfEvolution_9900049'],
    249: ['AncientWoods_WestDescent2_4', 'AncientWoods_WestDescent2_105'],
    250: ['MagmaChamber_South3_West_3'],
    251: ['MagmaChamber_North8_East_27900026'],
    252: ['BlueCave_ChampionRoom_Champion'],
    253: ['SunPalace_EastSewers6_7'],
    254: ['SunPalace_EastSewers6_5'],
    255: ['StrongholdDungeon_CentralHidden_3'],
    256: ['AncientWoods_Center5_4'],
    257: ['AncientWoods_Center6_8500062'],
    258: ['AncientWoods_North5_0'],
    259: ['AncientWoods_Center6_3'],
    260: ['AncientWoods_Center7_6'],
    261: ['AncientWoods_DarkRoom_3'],
    262: ['AncientWoods_South3_3', 'AncientWoods_South3_7'],
    263: ['AncientWoods_TorchesRoom_3', 'AncientWoods_TorchesRoom_7'],
    264: ['AncientWoods_East1_Shortcut_6'],
    265: ['AncientWoods_East3_Champion'],
    266: ['HorizonBeach_West1_0'],
    267: ['HorizonBeach_West3_0'],
    268: ['HorizonBeach_West3_3'],
    269: ['HorizonBeach_West4_3'],
    270: ['HorizonBeach_Center1_21900081'],
    271: ['HorizonBeach_Center1_3'],
    272: ['HorizonBeach_Labyrinth_28'],
    273: ['HorizonBeach_Labyrinth_27'],
    274: ['HorizonBeach_Center3_1'],
    275: ['HorizonBeach_Center3_5'],
    276: ['HorizonBeach_Center4_4'],
    277: ['HorizonBeach_Center4_9'],
    278: ['HorizonBeach_Center6_0'],
    279: ['HorizonBeach_East3_4'],
    280: ['HorizonBeach_East2_Lower_54', 'HorizonBeach_East2_Middle_57'],
    281: ['HorizonBeach_East2_Lower_55'],
    282: ['HorizonBeach_EastHidden_1'],
    283: ['HorizonBeach_EastChampion_1'],
    284: ['HorizonBeach_EastChampion_3', 'HorizonBeach_EastChampion_Champion'],
    285: ['HorizonBeach_East1_0'],
    286: ['HorizonBeach_Fisher_24300040'],
    287: ['HorizonBeach_Fisher_2'],
    288: ['HorizonBeach_East2_Middle_58'],
    289: ['HorizonBeach_East2_Upper_53'],
    290: ['HorizonBeach_East6_0'],
    291: ['HorizonBeach_East6_2'],
    292: ['HorizonBeach_East5_24500009'],
    293: ['HorizonBeach_East5_3'],
    294: ['HorizonBeach_East5_4'],
    295: ['HorizonBeach_Center5_6'],
    296: ['HorizonBeach_Center5_3'],
    297: ['HorizonBeach_Center2_5'],
    298: ['HorizonBeach_Center2_3'],
    299: ['HorizonBeach_South6_6'],
    300: ['HorizonBeach_South6_10'],
    301: ['HorizonBeach_South4_2'],
    302: ['HorizonBeach_TreasureCave2_2'],
    303: ['HorizonBeach_TreasureCave3_2'],
    304: ['HorizonBeach_TreasureCave5_3'],
    305: ['HorizonBeach_Champion_24200118'],
    306: ['HorizonBeach_Champion_7', 'HorizonBeach_Champion_24200124', 'HorizonBeach_Champion_Champion'],
    307: ['HorizonBeach_FWEntrance1_2'],
    308: ['ForgottenWorld_Jungle1_3'],
    309: ['ForgottenWorld_Jungle1_1'],
    310: ['ForgottenWorld_Caves1_1'],
    311: ['ForgottenWorld_Caves2_Lower_8'],
    312: ['ForgottenWorld_WandererRoom_45100110'],
    313: ['ForgottenWorld_MCPath1_0'],
    314: ['ForgottenWorld_MCPath2_12'],
    315: ['ForgottenWorld_MCPath3_3'],
    316: ['MagmaChamber_South9_East_8'],
    317: ['MagmaChamber_South8_0', 'MagmaChamber_South8_1'],
    318: ['ForgottenWorld_Caves5_Upper_4'],
    319: ['ForgottenWorld_Caves5_Upper_5'],
    320: ['ForgottenWorld_Caves5_Lower_12'],
    321: ['ForgottenWorld_Caves9_2'],
    322: ['ForgottenWorld_TerradrileLair1_2'],
    323: ['ForgottenWorld_TerradrileLair2_8'],
    324: ['ForgottenWorld_TerradrileLair2_3'],
    325: ['ForgottenWorld_TerradrileLair2_Champion'],
    326: ['ForgottenWorld_CavesStudy_50400001'],
    327: ['ForgottenWorld_Caves4_0'],
    328: ['ForgottenWorld_Caves6_5'],
    329: ['ForgottenWorld_Caves6_8'],
    330: ['ForgottenWorld_Caves12_0'],
    331: ['ForgottenWorld_DarkRoom_14'],
    332: ['ForgottenWorld_WorldTree_1', 'ForgottenWorld_WorldTree_46100009'],
    333: ['ForgottenWorld_TarPits5_Lower_1'],
    334: ['ForgottenWorld_TarPits9_0'],
    335: ['ForgottenWorld_TarPits4_52800001'],
    336: ['ForgottenWorld_TarPits4_1'],
    337: ['ForgottenWorld_TarPits3_1'],
    338: ['ForgottenWorld_TarPits3_0'],
    339: ['ForgottenWorld_TarPits1_1'],
    340: ['ForgottenWorld_Jungle5_Hidden_0'],
    341: ['ForgottenWorld_Jungle3_1'],
    342: ['ForgottenWorld_JungleHidden_23'],
    343: ['ForgottenWorld_Jungle6_3', 'ForgottenWorld_Jungle6_0'],
    344: ['ForgottenWorld_Jungle6_34'],
    345: ['ForgottenWorld_ClimbPuzzle_2'],
    346: ['ForgottenWorld_ClimbPuzzle_3'],
    347: ['ForgottenWorld_Climb1_46600001'],
    348: ['ForgottenWorld_Climb2_4'],
    349: ['ForgottenWorld_Climb2_3'],
    350: ['ForgottenWorld_Climb2_5'],
    351: ['ForgottenWorld_Climb3_3'],
    352: ['ForgottenWorld_Climb4_14'],
    353: ['ForgottenWorld_Climb4_9', 'ForgottenWorld_Climb4_10'],
    354: ['ForgottenWorld_Climb4_23', 'ForgottenWorld_Climb4_11'],
    355: ['ForgottenWorld_Climb4_13'],
    356: ['ForgottenWorld_ClimbSide_3'],
    357: ['ForgottenWorld_ClimbSide_1'],
    358: ['ForgottenWorld_Climb5_3'],
    359: ['ForgottenWorld_TarPits8_0'],
    360: ['StrongholdDungeon_JailHidden_2'],
    361: ['StrongholdDungeon_Library_14200159'],
    362: ['StrongholdDungeon_Library2_1', 'StrongholdDungeon_Library2_2'],
    363: ['StrongholdDungeon_WestHidden_3'],
    364: ['SnowyPeaks_Cryomancer_17900062', 'SnowyPeaks_Cryomancer_17900077', 'SnowyPeaks_Cryomancer_17900065',
          'SnowyPeaks_Cryomancer_17900066'],
    365: ['AncientWoods_East4_0', 'AncientWoods_East4_2'],
    366: ['AncientWoods_East4_4'],
    367: ['AncientWoods_South4_1'],
    368: ['BlueCave_South5_29300061', 'BlueCave_South5_29300065'],
    369: ['Underworld_East3_3'],
    370: ['Underworld_East3_4'],
    371: ['Underworld_East4_3'],
    372: ['Underworld_East5_2'],
    373: ['Underworld_EastCatacomb10_4'],
    374: ['Underworld_EastCatacomb10_5'],
    375: ['Underworld_EastCatacomb6_East_4'],
    376: ['Underworld_EastCatacomb5_9'],
    377: ['Underworld_EastCatacomb3_13'],
    378: ['Underworld_EastCatacomb4_3'],
    379: ['Underworld_EastCatacomb6_West_1'],
    380: ['Underworld_EastCatacomb9_1', 'Underworld_EastCatacomb9_4'],
    381: ['Underworld_Center1_29000021'],
    382: ['Underworld_Center2_7'],
    383: ['Underworld_WestCatacomb9_ExteriorEast_7'],
    384: ['Underworld_WestCatacomb1_8'],
    385: ['Underworld_WestCatacomb3_9'],
    386: ['Underworld_WestCatacomb4_Lower_8'],
    387: ['Underworld_WestCatacomb4_Lower_11'],
    388: ['Underworld_CenterHidden_0', 'Underworld_CenterHidden_1'],
    389: ['Underworld_Center3_2'],
    390: ['Underworld_WestCatacomb7_Shortcut_5'],
    391: ['Underworld_WestCatacomb9_ExteriorWest_11'],
    392: ['Underworld_WestCatacomb9_Roof_12'],
    393: ['Underworld_WestCatacomb9_Interior_Champion', 'Underworld_WestCatacomb9_Interior_32100074'],
    394: ['Underworld_West1_3'],
    395: ['Underworld_West6_1'],
    396: ['Underworld_West4_Champion'],
    397: ['Underworld_WestCatacomb10_0', 'Underworld_WestCatacomb10_3'],
    398: ['BlobBurg_East2_2'],
    399: ['BlobBurg_EastHidden_2'],
    400: ['BlobBurg_East3_1'],
    401: ['BlobBurg_Center1_8'],
    402: ['BlobBurg_Center2_0'],
    403: ['BlobBurg_Center2_41300001'],
    404: ['BlobBurg_East4_1'],
    405: ['BlobBurg_East5_41200001'],
    406: ['BlobBurg_Center3_41200001'],
    407: ['BlobBurg_Center4_4'],
    408: ['BlobBurg_South2_42000001'],
    409: ['BlobBurg_South2_0'],
    410: ['BlobBurg_South2_1'],
    411: ['BlobBurg_West1_1'],
    412: ['BlobBurg_West1_10'],
    413: ['BlobBurg_West1_3'],
    414: ['BlobBurg_West2_41700001'],
    415: ['BlobBurg_Champion_Champion', 'BlobBurg_Champion_42600001'],
    416: ['BlobBurg_Worms_3'],
    417: ['BlobBurg_Worms_4'],
    418: ['AncientWoods_North3_Champion'],
    419: ['AncientWoods_East4_0', 'AncientWoods_East4_2'],
    420: ['AncientWoods_South1_6'],
    421: ['MagmaChamber_Center11_15'],
    422: ['MagmaChamber_Center11_17'],
    423: ['MagmaChamber_South4_Lower_7'],
    424: ['MagmaChamber_Champion2_7'],
    425: ['MagmaChamber_Champion2_Champion', 'MagmaChamber_Champion2_0'],
    426: ['MagmaChamber_LegendaryKeeperRoom_43900165', 'MagmaChamber_LegendaryKeeperRoom_43900176',
          'MagmaChamber_LegendaryKeeperRoom_43900178', 'MagmaChamber_LegendaryKeeperRoom_43900179',
          'MagmaChamber_LegendaryKeeperRoom_43900180', 'MagmaChamber_LegendaryKeeperRoom_43900181'],
    427: ['MagmaChamber_South7_East_4'],
    428: ['MagmaChamber_South5_21'],
    429: ['MagmaChamber_Champion_Champion'],
    430: ['MagmaChamber_Champion_28600001'],
    431: ['MagmaChamber_South5_20'],
    432: ['MagmaChamber_South5_22'],
    433: ['MagmaChamber_TarPit_0'],
    434: ['ForgottenWorld_FallHidden_0', 'ForgottenWorld_FallHidden_2', 'ForgottenWorld_FallHidden_3'],
    435: ['MysticalWorkshop_Center1_Upper_33200006'],
    436: ['AbandonedTower_South2_1'],
    437: ['AbandonedTower_South3_Upper_1'],
    438: ['AbandonedTower_South5_3'],
    439: ['AbandonedTower_South7_3', 'AbandonedTower_South7_7'],
    440: ['AbandonedTower_SouthHidden2_0', 'AbandonedTower_SouthHidden2_3'],
    441: ['AbandonedTower_SouthHidden1_1'],
    442: ['AbandonedTower_South6_3'],
    443: ['AbandonedTower_Center2_3'],
    444: ['AbandonedTower_Center3_Upper_1'],
    445: ['AbandonedTower_Center3_Lower_11'],
    446: ['AbandonedTower_Center3_Lower_10'],
    447: ['AbandonedTower_South8_7'],
    448: ['AbandonedTower_South8_3'],
    449: ['AbandonedTower_Center5_4'],
    450: ['AbandonedTower_Center6_5'],
    451: ['AbandonedTower_Center10_5'],
    452: ['AbandonedTower_Center8_38300133'],
    453: ['AbandonedTower_Center9_8'],
    454: ['AbandonedTower_Center11_1', 'AbandonedTower_Center11_5'],
    455: ['AbandonedTower_Center12_7'],
    456: ['AbandonedTower_North1_38800022'],
    457: ['AbandonedTower_North4_5'],
    458: ['AbandonedTower_North3_5'],
    459: ['AbandonedTower_North5_8'],
    460: ['AbandonedTower_NorthHidden_1', 'AbandonedTower_NorthHidden_2'],
    461: ['AbandonedTower_North7_8'],
    462: ['AbandonedTower_North9_39700006'],
    463: ['AbandonedTower_Final_Champion'],
    464: ['KeeperStronghold_CenterStairwell_2300075'],
    465: ['SunPalace_North3_Champion'],
    466: ['AncientWoods_North3_10', 'AncientWoods_North3_11'],
    467: ['HorizonBeach_Pit_Secret_2'],
    468: ['MagmaChamber_PuppyRoom_44200172'],
    469: ['MysticalWorkshop_Vertraag_Champion'],
    470: ['ForgottenWorld_Waters1_Upper_5'],
    471: ['ForgottenWorld_Waters1_Lower_7'],
    472: ['ForgottenWorld_Waters5_4'],
    473: ['ForgottenWorld_Waters5_3'],
    474: ['ForgottenWorld_Waters2_4'],
    475: ['ForgottenWorld_Waters2_5'],
    476: ['ForgottenWorld_WatersHidden_11'],
    477: ['ForgottenWorld_DracomerLair_2'],
    478: ['ForgottenWorld_DracomerLair_Champion'],
}

map_tile_locations = {
    0: [('overview', 36, 28)],
    1: [('overview', 37, 28)],
    2: [('overview', 36, 27)],
    3: [('overview', 37, 27)],
    4: [('overview', 40, 27)],
    5: [('overview', 40, 29)],
    6: [('overview', 40, 30)],
    7: [('overview', 37, 29)],
    8: [('overview', 34, 29)],
    9: [('overview', 31, 31)],
    10: [('overview', 31, 30)],
    11: [('overview', 34, 31)],
    12: [('overview', 29, 29)],
    13: [('overview', 30, 30)],
    14: [('overview', 27, 30)],
    15: [('overview', 25, 28)],
    16: [('overview', 25, 32)],
    17: [('overview', 24, 32)],
    18: [('overview', 23, 31)],
    19: [('overview', 29, 28)],
    20: [('overview', 30, 28)],
    21: [('overview', 24, 28)],
    22: [('overview', 24, 29)],
    23: [('overview', 23, 28)],
    24: [('overview', 21, 29)],
    25: [('overview', 22, 30)],
    26: [('overview', 28, 32)],
    27: [('overview', 28, 33)],
    28: [('overview', 28, 31)],
    29: [('overview', 29, 31)],
    30: [('overview', 30, 31)],
    31: [('overview', 41, 30)],
    32: [('overview', 42, 30)],
    33: [('overview', 42, 32)],
    34: [('overview', 40, 31)],
    35: [('overview', 41, 31)],
    36: [('overview', 37, 33)],
    37: [('overview', 43, 32)],
    38: [('overview', 44, 32)],
    39: [('overview', 50, 30)],
    40: [('overview', 47, 28)],
    41: [('overview', 45, 27)],
    42: [('overview', 43, 28)],
    43: [('overview', 52, 28)],
    44: [('overview', 38, 35)],
    45: [('overview', 37, 35)],
    46: [('overview', 41, 35)],
    47: [('overview', 42, 35)],
    48: [('overview', 44, 34)],
    49: [('overview', 45, 33)],
    50: [('overview', 47, 33)],
    51: [('overview', 50, 34)],
    52: [('overview', 35, 34)],
    53: [('overview', 36, 34)],
    54: [('overview', 35, 35)],
    55: [('overview', 31, 32)],
    56: [('overview', 30, 32)],
    57: [('overview', 29, 32)],
    58: [('overview', 34, 34)],
    59: [('overview', 32, 35)],
    60: [('overview', 29, 36)],
    61: [('overview', 30, 36)],
    62: [('overview', 28, 35)],
    63: [('overview', 24, 34)],
    64: [('overview', 26, 36)],
    65: [('overview', 24, 37)],
    66: [('overview', 23, 37)],
    67: [('overview', 20, 37)],
    68: [('overview', 21, 39)],
    69: [('overview', 19, 39)],
    70: [('overview', 18, 40)],
    71: [('overview', 19, 41)],
    72: [('overview', 22, 41)],
    73: [('overview', 26, 39)],
    74: [('overview', 25, 37)],
    75: [('overview', 16, 41)],
    76: [('overview', 13, 41)],
    77: [('overview', 15, 39)],
    78: [('overview', 13, 39)],
    79: [('overview', 11, 38)],
    80: [('overview', 12, 38)],
    81: [('overview', 13, 37)],
    82: [('overview', 14, 34)],
    83: [('overview', 11, 34)],
    84: [('overview', 11, 33)],
    85: [('overview', 15, 37)],
    86: [('overview', 16, 36)],
    87: [('overview', 51, 30)],
    88: [('overview', 51, 31)],
    89: [('overview', 55, 30)],
    90: [('overview', 54, 31)],
    91: [('overview', 53, 31)],
    92: [('overview', 52, 32)],
    93: [('overview', 50, 33)],
    94: [('overview', 57, 31)],
    95: [('overview', 58, 35)],
    96: [('overview', 59, 29)],
    97: [('overview', 63, 29)],
    98: [('overview', 62, 30)],
    99: [('overview', 61, 30)],
    100: [('overview', 66, 30)],
    101: [('overview', 68, 30)],
    102: [('overview', 72, 29)],
    103: [('overview', 71, 30)],
    104: [('overview', 49, 36)],
    105: [('overview', 46, 37)],
    106: [('overview', 45, 36)],
    107: [('overview', 44, 36)],
    108: [('overview', 49, 37)],
    109: [('overview', 46, 38)],
    110: [('overview', 47, 39)],
    111: [('overview', 58, 30)],
    112: [('overview', 18, 32)],
    113: [('overview', 18, 35)],
    114: [('overview', 10, 30)],
    115: [('overview', 6, 29)],
    116: [('overview', 7, 27)],
    117: [('overview', 4, 27)],
    118: [('overview', 4, 28)],
    119: [('overview', 5, 28)],
    120: [('overview', 3, 26)],
    121: [('overview', 2, 27)],
    122: [('overview', 2, 26)],
    123: [('overview', 3, 25)],
    124: [('overview', 4, 29)],
    125: [('overview', 0, 28)],
    126: [('overview', 0, 29)],
    127: [('overview', 3, 24)],
    128: [('overview', 5, 24)],
    129: [('overview', 5, 23)],
    130: [('overview', 6, 24)],
    131: [('overview', 5, 21)],
    132: [('overview', 5, 20)],
    133: [('overview', 6, 20)],
    134: [('overview', 4, 19)],
    135: [('overview', 14, 21)],
    136: [('overview', 15, 21)],
    137: [('overview', 16, 21)],
    138: [('overview', 17, 22)],
    139: [('overview', 15, 23)],
    140: [('overview', 17, 23)],
    141: [('overview', 17, 24)],
    142: [('overview', 18, 25)],
    143: [('overview', 18, 26)],
    144: [('overview', 17, 27)],
    145: [('overview', 16, 24)],
    146: [('overview', 16, 25)],
    147: [('overview', 15, 24)],
    148: [('overview', 15, 25)],
    149: [('overview', 15, 26)],
    150: [('overview', 15, 27)],
    151: [('overview', 14, 28)],
    152: [('overview', 13, 29)],
    153: [('overview', 10, 28)],
    154: [('overview', 15, 30)],
    155: [('overview', 17, 29)],
    156: [('overview', 18, 29)],
    157: [('overview', 19, 29)],
    158: [('overview', 18, 30)],
    159: [('overview', 59, 32)],
    160: [('overview', 59, 33)],
    161: [('overview', 60, 35)],
    162: [('overview', 57, 35)],
    163: [('overview', 56, 35)],
    164: [('overview', 56, 38)],
    165: [('overview', 54, 37)],
    166: [('overview', 52, 34)],
    167: [('overview', 52, 37)],
    168: [('overview', 56, 39)],
    169: [('overview', 57, 39)],
    170: [('overview', 60, 38)],
    171: [('overview', 61, 37)],
    172: [('overview', 61, 38)],
    173: [('overview', 62, 40)],
    174: [('overview', 61, 39)],
    175: [('overview', 64, 38)],
    176: [('overview', 63, 37)],
    177: [('overview', 69, 39)],
    178: [('overview', 70, 42)],
    179: [('overview', 71, 39)],
    180: [('overview', 74, 38)],
    181: [('overview', 74, 37)],
    182: [('overview', 77, 35)],
    183: [('overview', 79, 36)],
    184: [('overview', 81, 35)],
    185: [('overview', 82, 34)],
    186: [('overview', 88, 35)],
    187: [('overview', 87, 36)],
    188: [('overview', 67, 32)],
    189: [('overview', 68, 33)],
    190: [('overview', 69, 33)],
    191: [('overview', 65, 32)],
    192: [('overview', 66, 34)],
    193: [('overview', 68, 34)],
    194: [('overview', 72, 32)],
    195: [('overview', 74, 32)],
    196: [('overview', 64, 35)],
    197: [('overview', 65, 36)],
    198: [('overview', 61, 35)],
    199: [('overview', 58, 28)],
    200: [('overview', 60, 28)],
    201: [('overview', 57, 28)],
    202: [('overview', 55, 28)],
    203: [('overview', 61, 27)],
    204: [('overview', 58, 25)],
    205: [('overview', 61, 24)],
    206: [('overview', 59, 22)],
    207: [('overview', 60, 23)],
    208: [('overview', 59, 24)],
    209: [('overview', 61, 23)],
    210: [('overview', 58, 21)],
    211: [('overview', 58, 24)],
    212: [('overview', 61, 22)],
    213: [('overview', 61, 21)],
    214: [('overview', 59, 20)],
    215: [('overview', 60, 20)],
    216: [('overview', 61, 19)],
    217: [('overview', 63, 19)],
    218: [('overview', 62, 21)],
    219: [('overview', 61, 18)],
    220: [('overview', 60, 17)],
    221: [('overview', 59, 19)],
    222: [('overview', 60, 18)],
    223: [('overview', 57, 20)],
    224: [('overview', 57, 17)],
    225: [('overview', 59, 16)],
    226: [('overview', 57, 16)],
    227: [('overview', 60, 16)],
    228: [('overview', 70, 33)],
    229: [('overview', 70, 32)],
    230: [('overview', 41, 27)],
    231: [('overview', 48, 26)],
    232: [('overview', 84, 36)],
    233: [('overview', 76, 41)],
    234: [('overview', 77, 40)],
    235: [('overview', 75, 39)],
    236: [('overview', 78, 39)],
    237: [('overview', 79, 39)],
    238: [('overview', 78, 42)],
    239: [('overview', 75, 42)],
    240: [('overview', 82, 42)],
    241: [('overview', 81, 40)],
    242: [('overview', 80, 39)],
    243: [('overview', 83, 39)],
    244: [('overview', 86, 38)],
    245: [('overview', 87, 40)],
    246: [('overview', 65, 29)],
    247: [('overview', 67, 29)],
    248: [('overview', 66, 29)],
    249: [('overview', 66, 38)],
    250: [('overview', 85, 41)],
    251: [('overview', 81, 37)],
    252: [('overview', 41, 33)],
    253: [('overview', 24, 41)],
    254: [('overview', 25, 41)],
    255: [('overview', 60, 36)],
    256: [('overview', 76, 30)],
    257: [('overview', 78, 30)],
    258: [('overview', 76, 29)],
    259: [('overview', 79, 30)],
    260: [('overview', 82, 31)],
    261: [('overview', 83, 33)],
    262: [('overview', 78, 34)],
    263: [('overview', 77, 33)],
    264: [('overview', 83, 29)],
    265: [('overview', 88, 29)],
    266: [('overview', 93, 30)],
    267: [('overview', 96, 28)],
    268: [('overview', 97, 28)],
    269: [('overview', 98, 30)],
    270: [('overview', 102, 30)],
    271: [('overview', 102, 31)],
    272: [('overview', 107, 34)],
    273: [('overview', 105, 34)],
    274: [('overview', 108, 31)],
    275: [('overview', 109, 32)],
    276: [('overview', 111, 32)],
    277: [('overview', 112, 32)],
    278: [('overview', 114, 30)],
    279: [('overview', 116, 31)],
    280: [('overview', 118, 29)],
    281: [('overview', 120, 31)],
    282: [('overview', 121, 33)],
    283: [('overview', 120, 33)],
    284: [('overview', 119, 33)],
    285: [('overview', 117, 29)],
    286: [('overview', 123, 30)],
    287: [('overview', 124, 30)],
    288: [('overview', 120, 29)],
    289: [('overview', 120, 28)],
    290: [('overview', 118, 26)],
    291: [('overview', 117, 26)],
    292: [('overview', 122, 25)],
    293: [('overview', 123, 25)],
    294: [('overview', 124, 25)],
    295: [('overview', 115, 32)],
    296: [('overview', 115, 33)],
    297: [('overview', 107, 29)],
    298: [('overview', 105, 29)],
    299: [('overview', 104, 36)],
    300: [('overview', 103, 36)],
    301: [('overview', 97, 33)],
    302: [('overview', 95, 34)],
    303: [('overview', 94, 34)],
    304: [('overview', 94, 36)],
    305: [('overview', 92, 36)],
    306: [('overview', 91, 36)],
    307: [('overview', 96, 36)],
    308: [('overview', 105, 45)],
    309: [('overview', 105, 46)],
    310: [('overview', 103, 46)],
    311: [('overview', 102, 49)],
    312: [('overview', 99, 47)],
    313: [('overview', 100, 47)],
    314: [('overview', 98, 44)],
    315: [('overview', 97, 43)],
    316: [('overview', 96, 42)],
    317: [('overview', 93, 42)],
    318: [('overview', 103, 49)],
    319: [('overview', 103, 50)],
    320: [('overview', 103, 51)],
    321: [('overview', 101, 52)],
    322: [('overview', 97, 55)],
    323: [('overview', 99, 56)],
    324: [('overview', 100, 56)],
    325: [('overview', 101, 56)],
    326: [('overview', 97, 52)],
    327: [('overview', 104, 49)],
    328: [('overview', 106, 49)],
    329: [('overview', 105, 50)],
    330: [('overview', 107, 52)],
    331: [('overview', 105, 52)],
    332: [('overview', 108, 49)],
    333: [('overview', 115, 50)],
    334: [('overview', 118, 51)],
    335: [('overview', 117, 49)],
    336: [('overview', 119, 49)],
    337: [('overview', 120, 49)],
    338: [('overview', 120, 48)],
    339: [('overview', 117, 47)],
    340: [('overview', 115, 46)],
    341: [('overview', 110, 45)],
    342: [('overview', 106, 45)],
    343: [('overview', 118, 43)],
    344: [('overview', 117, 42)],
    345: [('overview', 120, 41)],
    346: [('overview', 120, 40)],
    347: [('overview', 119, 40)],
    348: [('overview', 118, 40)],
    349: [('overview', 118, 38)],
    350: [('overview', 118, 37)],
    351: [('overview', 116, 37)],
    352: [('overview', 115, 37)],
    353: [('overview', 115, 35)],
    354: [('overview', 113, 37)],
    355: [('overview', 113, 36)],
    356: [('overview', 111, 36)],
    357: [('overview', 108, 36)],
    358: [('overview', 112, 35)],
    359: [('overview', 114, 47)],
    360: [('overview', 52, 31)],
    361: [('overview', 56, 39)],
    362: [('overview', 57, 39)],
    363: [('overview', 51, 35)],
    364: [('overview', 5, 26)],
    365: [('overview', 87, 27)],
    366: [('overview', 87, 26)],
    367: [('overview', 78, 32)],
    368: [('overview', 49, 39)],
    369: [('overview', 45, 41)],
    370: [('overview', 44, 41)],
    371: [('overview', 43, 43)],
    372: [('overview', 41, 43)],
    373: [('overview', 41, 44)],
    374: [('overview', 42, 44)],
    375: [('overview', 38, 45)],
    376: [('overview', 37, 44)],
    377: [('overview', 37, 42)],
    378: [('overview', 38, 41)],
    379: [('overview', 37, 45)],
    380: [('overview', 38, 38)],
    381: [('overview', 36, 43)],
    382: [('overview', 34, 42)],
    383: [('overview', 31, 41)],
    384: [('overview', 29, 43)],
    385: [('overview', 28, 44)],
    386: [('overview', 29, 45)],
    387: [('overview', 31, 45)],
    388: [('overview', 36, 44)],
    389: [('overview', 35, 45)],
    390: [('overview', 28, 43)],
    391: [('overview', 29, 41)],
    392: [('overview', 29, 40)],
    393: [('overview', 30, 41)],
    394: [('overview', 26, 42)],
    395: [('overview', 20, 44)],
    396: [('overview', 21, 43)],
    397: [('overview', 32, 43)],
    398: [('overview', 66, 41)],
    399: [('overview', 65, 41)],
    400: [('overview', 65, 43)],
    401: [('overview', 63, 42)],
    402: [('overview', 62, 45)],
    403: [('overview', 60, 45)],
    404: [('overview', 64, 45)],
    405: [('overview', 66, 46)],
    406: [('overview', 61, 42)],
    407: [('overview', 58, 46)],
    408: [('overview', 62, 46)],
    409: [('overview', 62, 47)],
    410: [('overview', 63, 47)],
    411: [('overview', 57, 47)],
    412: [('overview', 56, 47)],
    413: [('overview', 55, 47)],
    414: [('overview', 54, 43)],
    415: [('overview', 56, 44)],
    416: [('overview', 58, 42)],
    417: [('overview', 60, 41)],
    418: [('overview', 82, 28)],
    419: [('overview', 83, 28)],
    420: [('overview', 81, 32)],
    421: [('overview', 90, 39)],
    422: [('overview', 90, 38)],
    423: [('overview', 89, 41)],
    424: [('overview', 91, 40)],
    425: [('overview', 93, 40)],
    426: [('overview', 94, 39)],
    427: [('overview', 92, 42)],
    428: [('overview', 86, 43)],
    429: [('overview', 85, 43)],
    430: [('overview', 84, 43)],
    431: [('overview', 86, 41)],
    432: [('overview', 86, 40)],
    433: [('overview', 88, 43)],
    434: [('overview', 100, 41)],
    435: [('overview', 60, 25)],
    436: [('overview', 53, 23)],
    437: [('overview', 55, 22)],
    438: [('overview', 55, 20)],
    439: [('overview', 54, 20)],
    440: [('overview', 55, 19)],
    441: [('overview', 53, 20)],
    442: [('overview', 53, 18)],
    443: [('overview', 53, 15)],
    444: [('overview', 55, 13)],
    445: [('overview', 55, 15)],
    446: [('overview', 55, 16)],
    447: [('overview', 54, 17)],
    448: [('overview', 55, 18)],
    449: [('overview', 58, 12)],
    450: [('overview', 54, 12)],
    451: [('overview', 55, 10)],
    452: [('overview', 55, 11)],
    453: [('overview', 57, 11)],
    454: [('overview', 56, 9)],
    455: [('overview', 54, 8)],
    456: [('overview', 56, 7)],
    457: [('overview', 55, 5)],
    458: [('overview', 56, 6)],
    459: [('overview', 57, 7)],
    460: [('overview', 56, 3)],
    461: [('overview', 57, 3)],
    462: [('overview', 56, 1)],
    463: [('overview', 56, 0)],
    464: [('overview', 48, 28)],
    465: [('overview', 16, 34)],
    466: [('overview', 83, 28)],
    467: [('overview', 94, 33)],
    468: [('overview', 87, 38)],
    469: [('overview', 58, 16)],
    470: [('overview', 112, 50)],
    471: [('overview', 112, 52)],
    472: [('overview', 114, 51)],
    473: [('overview', 114, 50)],
    474: [('overview', 111, 53)],
    475: [('overview', 111, 54)],
    476: [('overview', 110, 53)],
    477: [('overview', 110, 51)],
    478: [('overview', 111, 51)]
}

sub_map_offsets = {
    'abandoned_tower': (53, 0),
    'ancient_woods': (61, 26),
    'blob_burg': (54, 41),
    'blue_caves': (29, 30),
    'forgotten_world': (97, 33),
    'horizon_beach': (89, 25),
    'keepers_stronghold': (43, 24),
    'mystical_workshop': (54, 15),
    'magma_chamber': (67, 34),
    'mountain_path': (21, 27),
    'snowy_peaks': (0, 19),
    'sun_palace': (11, 32),
    'stronghold_dungeon': (49, 28),
    'the_underworld': (20, 38)
}


def fix_mapping_table():
    for k, v in map_location_mapping.items():
        map_location_mapping[k] = [loc_names[v2] for v2 in v]


fix_mapping_table()


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


__regions_by_locs = {}


def setup_regions_by_locs():
    if len(__regions_by_locs) > 0:
        return
    with open('data/world.json', mode='r') as f:
        json_data = json.load(f)
    for current_region_data in json_data:
        region = current_region_data['region']
        for chest_data in current_region_data.get("chests") or []:
            # Hack because we store comments as strings
            if isinstance(chest_data, str):
                continue
            __regions_by_locs[loc_names[f"{region}_{chest_data['id']}"]] = region

        for gift_data in current_region_data.get("gifts") or []:
            # Hack because we store comments as strings
            if isinstance(gift_data, str):
                continue
            __regions_by_locs[loc_names[f"{region}_{gift_data['id']}"]] = region

        for champion_data in current_region_data.get("champion") or []:
            # Hack because we store comments as strings
            if isinstance(champion_data, str):
                continue
            __regions_by_locs[loc_names[f'{region}_Champion']] = region

        for flag_data in current_region_data.get("flags") or []:
            # Hack because we store comments as strings
            if isinstance(flag_data, str):
                continue
            # __regions_by_locs[loc_names[f"Flag {region}_{flag_data['id']}"]] = region


def adjust_pos(pos):
    offset_x = 0
    offset_y = 0
    if pos[0] in sub_map_offsets.keys():
        offset_x += SUB_MAP_OFFSET
        offset_y += SUB_MAP_OFFSET
    return pos[0], pos[1] * TILE_SIZE + (TILE_SIZE // 2) + offset_x, pos[2] * TILE_SIZE + (TILE_SIZE // 2) + offset_y


submap_override_values = {
    "KeeperStronghold": 'keepers_stronghold',
    "BlueCave":  'blue_caves',
    "Underworld": 'the_underworld'
}
def convert_region_to_sub_map(region):
    tmp = region.split("_")[0]
    if tmp in submap_override_values :
        return submap_override_values[tmp]
    return '_'.join(re.findall('[A-Z][^A-Z]*', tmp)).lower()


def get_sub_map_locs(region, map_locs_mappings):
    new_mappings = []
    sub_map = convert_region_to_sub_map(region)
    sub_map_offset = sub_map_offsets[sub_map]
    if sub_map is None:
        return
    for v in map_locs_mappings:
        new_mappings.append((sub_map, v[1]-sub_map_offset[0], v[2]-sub_map_offset[1]))
    return new_mappings


def create_loc(locs: list[PopTrackerLocation], region: str, check_type_name, data, location_id,
               ids_for_sections, loc_names, postgame_data, count=1, clear_as_group=False):
    unopened_img = None
    opened_img = None
    if check_type_name == "Rank":
        unopened_img = 'images/items/rank/champion_defeated.png'
        opened_img = 'images/items/rank/champion_defeated_grey.png'
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
    map_locs_mappings = None
    mapping_values = None
    multi_sec = False
    for k, v in map_location_mapping.items():
        if loc_name in v:
            map_locs_mappings = map_tile_locations[k]
            map_locs_mappings += get_sub_map_locs(region, map_locs_mappings)
            mapping_values = v
            multi_sec = len(v) > 1
            break
    if map_locs_mappings is not None:
        map_locs = list(map(lambda x: PopTrackerMapLocation(*adjust_pos(x)), map_locs_mappings))
    access_rules: list[list[str]] = combine_access([[f"$has_access_to|{region}"]], get_access(data.get('requirements')),
                                                   "AND")
    visibilty_rules = None
    if f"{region}_{data['id']}" in postgame_data:
        visibilty_rules = [['$is_goal_not_mad_lord']]
    if multi_sec:
        parent_count = 1
        # parent_region, regions = get_common_region_name(mapping_values)
        parent_region = format_region_name(mapping_values)
        # if f'{region}_{data["id"]}' in subsections:
        #     parent_region = subsections[f'{region}_{data["id"]}']
        #     parent_region = parent_region[:parent_region.rfind("_")]
        temp_parent_name = parent_region
        parent_region = f'{temp_parent_name}'
        while True:
            loc = next((x for x in locs if x.name == parent_region), None)
            if loc is not None:
                first_sec = loc.sections[0]
                if first_sec.name not in mapping_values:
                    parent_count += 1
                    parent_region = f'{temp_parent_name} #{parent_count}'
                else:
                    break
            else:
                break
        if loc is None:
            # ToDo: format parent region name
            loc = PopTrackerLocation(parent_region, map_locations=map_locs)
            locs.append(loc)
        sec = PopTrackerSection(loc_name, item_count=count, clear_as_group=clear_as_group, access_rules=access_rules,
                                visibility_rules=visibilty_rules, chest_unopened_img=unopened_img,
                                chest_opened_img=opened_img)
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
        loc.sections.append(
            PopTrackerSection("", item_count=count, clear_as_group=clear_as_group, chest_unopened_img=unopened_img,
                              chest_opened_img=opened_img))
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


def format_region_name(mappings: list[str]):
    name = commonprefix([(v if len(v.split(' - ')) <= 2 else ' - '.join(v.split(' - ')[:-1])) for v in mappings]).strip(
        ' - ').strip()
    if name == 'Magma Chamber - Forgotten World Exit':
        name = 'Magma Chamber - Forgotten World Exit - Hidden'
    return name


def find_loc_with_same_map_loc(locs: list[PopTrackerLocation], map_locs: list[PopTrackerMapLocation]):
    for loc in locs:
        for map_loc in map_locs:
            if map_loc in loc.map_locations:
                return loc
    return None


def get_chest_loc(locs: list[PopTrackerLocation], region: str, data, location_id, ids_for_sections, loc_names,
                  postgame_data):
    loc, location_id = create_loc(locs, region, 'Chest', data, location_id, ids_for_sections, loc_names, postgame_data)
    return loc, location_id


def get_gift_loc(locs: list[PopTrackerLocation], region: str, data, location_id, ids_for_sections, loc_names,
                 postgame_data):
    loc, location_id = create_loc(locs, region, 'Gift', data, location_id, ids_for_sections, loc_names, postgame_data)
    return loc, location_id


def get_encounter_locs(locs: list[PopTrackerLocation], region: str, data, location_id, ids_for_sections, loc_names,
                       postgame_data):
    loc, location_id = create_loc(locs, region, 'Encounter', data, location_id, ids_for_sections, loc_names,
                                  postgame_data, count=3, clear_as_group=True)
    return loc, location_id


def get_champ_locs(locs: list[PopTrackerLocation], region: str, data, location_id, ids_for_sections, subsections,
                   postgame_data):
    loc, location_id = create_loc(locs, region, 'Rank', data, location_id, ids_for_sections, subsections, postgame_data)
    # loc, location_id = create_loc(locs, region, 'Champion', data, location_id, ids_for_sections, postgame_data, count=3,
    #                               clear_as_group=True)
    # location_id += 3
    return loc, location_id


def get_flag_loc(locs: list[PopTrackerLocation], region: str, data, subsections, postgame_data):
    loc, _ = create_loc(locs, region, 'Flag', data, None, None, subsections, postgame_data)
    return loc, None


locs_by_id = {}


def gen_locations():
    with open('data/postgame.json', mode='r') as f:
        postgame_data = json.load(f)
    with open('data/world.json', mode='r') as f:
        json_data = json.load(f)
    locs: list[PopTrackerLocation] = []
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
                                                  loc_names, postgame_data)

        for gift_data in current_region_data.get("gifts") or []:
            # Hack because we store comments as strings
            if isinstance(gift_data, str):
                continue
            location, location_id = get_gift_loc(locs, region_name, gift_data, location_id, ids_for_sections,
                                                 loc_names, postgame_data)

        for encounter_data in current_region_data.get("encounters") or []:
            # Hack because we store comments as strings
            if isinstance(encounter_data, str):
                continue
            # location, location_id = get_encounter_locs(locs, region_name, encounter_data, location_id, ids_for_sections,
            #                                            loc_names, postgame_data)

        for champion_data in current_region_data.get("champion") or []:
            # Hack because we store comments as strings
            if isinstance(champion_data, str):
                continue
            location, location_id = get_champ_locs(locs, region_name, champion_data, location_id, ids_for_sections,
                                                   loc_names, postgame_data)

        for flag_data in current_region_data.get("flags") or []:
            # Hack because we store comments as strings
            if isinstance(flag_data, str):
                continue
            location, _ = get_flag_loc(locs, region_name, flag_data, loc_names, postgame_data)

        # locs.append(region)
    with open('data/plotless.json', mode='r') as f:
        json_data = json.load(f)
    for plotless_data in json_data:
        loc_type = plotless_data['type']
        if loc_type == 'connection':
            continue  # handled by logic
        region_name = plotless_data['region']
        if loc_type == 'location':
            loc_type = 'Gift'  # ToDo: determine by id range
            loc_id = plotless_data['object_id']
        else:
            continue  # ToDo?
        loc_name = loc_names[f'{region_name}_{loc_id}']
        loc = loc_by_name[loc_name]
        loc.access_rules = combine_access(loc.access_rules,
                                          combine_access(
                                              [[f'$has_access_to|{region_name}', '$plotless']],
                                              get_access(plotless_data['requirements']), 'AND')
                                          , 'OR')
    # Fix sections sorting
    # ToDo: could probably be optimized...
    for loc in locs:
        loc.sections.sort(key=compare_section_order)
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


def compare_section_order(x: PopTrackerSection):
    for k, v in map_location_mapping.items():
        if x.name in v:
            return v.index(x.name)
    return 0


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
