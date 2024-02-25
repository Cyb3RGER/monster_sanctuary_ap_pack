import enum
import json
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
    295: ['HorizonBeach_Center5_3'],
    296: ['HorizonBeach_Center5_6'],
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
    97: [(MAIN_MAP_NAME, 1592 - TILE_SIZE * 2, 728)],
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
    228: [(MAIN_MAP_NAME, 1710, 800 + TILE_SIZE)],
    229: [(MAIN_MAP_NAME, 1710, 800)],
    230: [(MAIN_MAP_NAME, 1016, 678)],
    231: [(MAIN_MAP_NAME, 1184, 654)],
    232: [(MAIN_MAP_NAME, 2046, 894)],
    233: [(MAIN_MAP_NAME, 1856, 1016)],
    234: [(MAIN_MAP_NAME, 1856 + TILE_SIZE, 1016 - TILE_SIZE)],
    235: [(MAIN_MAP_NAME, 1832, 968)],
    236: [(MAIN_MAP_NAME, 1832 + TILE_SIZE * 3, 968)],
    237: [(MAIN_MAP_NAME, 1832 + TILE_SIZE * 4, 968)],
    238: [(MAIN_MAP_NAME, 1904, 1040)],
    239: [(MAIN_MAP_NAME, 1904 - TILE_SIZE * 3, 1040)],
    240: [(MAIN_MAP_NAME, 2000, 1040)],
    241: [(MAIN_MAP_NAME, 2000 - TILE_SIZE, 1040 - TILE_SIZE * 2)],
    242: [(MAIN_MAP_NAME, 2000 - TILE_SIZE * 2, 1040 - TILE_SIZE * 3)],
    243: [(MAIN_MAP_NAME, 2024, 968)],
    244: [(MAIN_MAP_NAME, 2096, 968 - TILE_SIZE)],
    245: [(MAIN_MAP_NAME, 2120, 968 + TILE_SIZE)],
    246: [(MAIN_MAP_NAME, 1592, 728)],
    247: [(MAIN_MAP_NAME, 1592 + TILE_SIZE * 2, 728)],
    248: [(MAIN_MAP_NAME, 1592 + TILE_SIZE, 728)],
    249: [(MAIN_MAP_NAME, 1616, 942)],
    250: [(MAIN_MAP_NAME, 2072, 1016)],
    251: [(MAIN_MAP_NAME, 1976, 920)],
    252: [(MAIN_MAP_NAME, 1014, 822)],
    253: [(MAIN_MAP_NAME, 608, 1018)],
    254: [(MAIN_MAP_NAME, 608 + TILE_SIZE, 1018)],
    255: [(MAIN_MAP_NAME, 1472, 872 + TILE_SIZE)],
    256: [(MAIN_MAP_NAME, 1856, 750)],
    257: [(MAIN_MAP_NAME, 1856 + TILE_SIZE * 2, 750)],
    258: [(MAIN_MAP_NAME, 1856, 750 - TILE_SIZE)],
    259: [(MAIN_MAP_NAME, 1856 + TILE_SIZE * 3, 750)],
    260: [(MAIN_MAP_NAME, 2000, 774)],
    261: [(MAIN_MAP_NAME, 2024, 774 + TILE_SIZE * 2)],
    262: [(MAIN_MAP_NAME, 1904, 846)],
    263: [(MAIN_MAP_NAME, 1904 - TILE_SIZE, 846 - TILE_SIZE)],
    264: [(MAIN_MAP_NAME, 2024, 724)],
    265: [(MAIN_MAP_NAME, 2144, 724)],
    266: [(MAIN_MAP_NAME, 2264, 748)],
    267: [(MAIN_MAP_NAME, 2336, 700)],
    268: [(MAIN_MAP_NAME, 2360, 700)],
    269: [(MAIN_MAP_NAME, 2384, 748)],
    270: [(MAIN_MAP_NAME, 2480, 748)],
    271: [(MAIN_MAP_NAME, 2480, 772)],
    272: [(MAIN_MAP_NAME, 2600, 844)],
    273: [(MAIN_MAP_NAME, 2552, 844)],
    274: [(MAIN_MAP_NAME, 2624, 772)],
    275: [(MAIN_MAP_NAME, 2648, 796)],
    276: [(MAIN_MAP_NAME, 2696, 796)],
    277: [(MAIN_MAP_NAME, 2720, 796)],
    278: [(MAIN_MAP_NAME, 2768, 748)],
    279: [(MAIN_MAP_NAME, 2816, 772)],
    280: [(MAIN_MAP_NAME, 2864, 724)],
    281: [(MAIN_MAP_NAME, 2912, 772)],
    282: [(MAIN_MAP_NAME, 2936, 820)],
    283: [(MAIN_MAP_NAME, 2912, 820)],
    284: [(MAIN_MAP_NAME, 2888, 820)],
    285: [(MAIN_MAP_NAME, 2840, 724)],
    286: [(MAIN_MAP_NAME, 2984, 748)],
    287: [(MAIN_MAP_NAME, 3008, 748)],
    288: [(MAIN_MAP_NAME, 2912, 724)],
    289: [(MAIN_MAP_NAME, 2912, 700)],
    290: [(MAIN_MAP_NAME, 2864, 652)],
    291: [(MAIN_MAP_NAME, 2840, 652)],
    292: [(MAIN_MAP_NAME, 2960, 628)],
    293: [(MAIN_MAP_NAME, 2984, 628)],
    294: [(MAIN_MAP_NAME, 3008, 628)],
    295: [(MAIN_MAP_NAME, 2792, 796)],
    296: [(MAIN_MAP_NAME, 2792, 820)],
    297: [(MAIN_MAP_NAME, 2600, 724)],
    298: [(MAIN_MAP_NAME, 2552, 724)],
    299: [(MAIN_MAP_NAME, 2528, 892)],
    300: [(MAIN_MAP_NAME, 2504, 892)],
    301: [(MAIN_MAP_NAME, 2360, 820)],
    302: [(MAIN_MAP_NAME, 2312, 844)],
    303: [(MAIN_MAP_NAME, 2288, 844)],
    304: [(MAIN_MAP_NAME, 2288, 892)],
    305: [(MAIN_MAP_NAME, 2240, 892)],
    306: [(MAIN_MAP_NAME, 2216, 892)],
    307: [(MAIN_MAP_NAME, 2336, 892)],
    308: [(MAIN_MAP_NAME, 2552, 1108)],
    309: [(MAIN_MAP_NAME, 2552, 1132)],
    310: [(MAIN_MAP_NAME, 2504, 1132)],
    311: [(MAIN_MAP_NAME, 2480, 1204)],
    312: [(MAIN_MAP_NAME, 2408, 1156)],
    313: [(MAIN_MAP_NAME, 2432, 1156)],
    314: [(MAIN_MAP_NAME, 2384, 1084)],
    315: [(MAIN_MAP_NAME, 2360, 1060)],
    316: [(MAIN_MAP_NAME, 2336, 1036)],
    317: [(MAIN_MAP_NAME, 2264, 1036)],
    318: [(MAIN_MAP_NAME, 2504, 1204)],
    319: [(MAIN_MAP_NAME, 2504, 1228)],
    320: [(MAIN_MAP_NAME, 2504, 1252)],
    321: [(MAIN_MAP_NAME, 2456, 1276)],
    322: [(MAIN_MAP_NAME, 2360, 1348)],
    323: [(MAIN_MAP_NAME, 2408, 1372)],
    324: [(MAIN_MAP_NAME, 2432, 1372)],
    325: [(MAIN_MAP_NAME, 2456, 1372)],
    326: [(MAIN_MAP_NAME, 2360, 1276)],
    327: [(MAIN_MAP_NAME, 2528, 1204)],
    328: [(MAIN_MAP_NAME, 2576, 1204)],
    329: [(MAIN_MAP_NAME, 2552, 1228)],
    330: [(MAIN_MAP_NAME, 2600, 1276)],
    331: [(MAIN_MAP_NAME, 2552, 1276)],
    332: [(MAIN_MAP_NAME, 2624, 1204)],
    333: [(MAIN_MAP_NAME, 2792, 1228)],
    334: [(MAIN_MAP_NAME, 2864, 1252)],
    335: [(MAIN_MAP_NAME, 2840, 1204)],
    336: [(MAIN_MAP_NAME, 2888, 1204)],
    337: [(MAIN_MAP_NAME, 2912, 1204)],
    338: [(MAIN_MAP_NAME, 2912, 1180)],
    339: [(MAIN_MAP_NAME, 2840, 1156)],
    340: [(MAIN_MAP_NAME, 2792, 1132)],
    341: [(MAIN_MAP_NAME, 2672, 1108)],
    342: [(MAIN_MAP_NAME, 2576, 1108)],
    343: [(MAIN_MAP_NAME, 2864, 1060)],
    344: [(MAIN_MAP_NAME, 2840, 1036)],
    345: [(MAIN_MAP_NAME, 2912, 1012)],
    346: [(MAIN_MAP_NAME, 2912, 988)],
    347: [(MAIN_MAP_NAME, 2888, 988)],
    348: [(MAIN_MAP_NAME, 2864, 988)],
    349: [(MAIN_MAP_NAME, 2864, 940)],
    350: [(MAIN_MAP_NAME, 2864, 916)],
    351: [(MAIN_MAP_NAME, 2816, 916)],
    352: [(MAIN_MAP_NAME, 2792, 916)],
    353: [(MAIN_MAP_NAME, 2792, 868)],
    354: [(MAIN_MAP_NAME, 2744, 916)],
    355: [(MAIN_MAP_NAME, 2744, 892)],
    356: [(MAIN_MAP_NAME, 2696, 892)],
    357: [(MAIN_MAP_NAME, 2624, 892)],
    358: [(MAIN_MAP_NAME, 2720, 868)],
    359: [(MAIN_MAP_NAME, 2768, 1156)],
    360: [(MAIN_MAP_NAME, 1280, 772)],
    361: [(MAIN_MAP_NAME, 1376, 964)],
    362: [(MAIN_MAP_NAME, 1400, 964)],
    363: [(MAIN_MAP_NAME, 1256, 868)],
    364: [(MAIN_MAP_NAME, 152, 652)],
    365: [(MAIN_MAP_NAME, 2120, 676)],
    366: [(MAIN_MAP_NAME, 2120, 652)],
    367: [(MAIN_MAP_NAME, 1904, 798)],
    368: [(MAIN_MAP_NAME, 1208, 964)],
    369: [(MAIN_MAP_NAME, 1112, 1012)],
    370: [(MAIN_MAP_NAME, 1088, 1012)],
    371: [(MAIN_MAP_NAME, 1064, 1060)],
    372: [(MAIN_MAP_NAME, 1016, 1060)],
    373: [(MAIN_MAP_NAME, 1016, 1084)],
    374: [(MAIN_MAP_NAME, 1040, 1084)],
    375: [(MAIN_MAP_NAME, 944, 1108)],
    376: [(MAIN_MAP_NAME, 920, 1084)],
    377: [(MAIN_MAP_NAME, 920, 1036)],
    378: [(MAIN_MAP_NAME, 944, 1012)],
    379: [(MAIN_MAP_NAME, 920, 1108)],
    380: [(MAIN_MAP_NAME, 944, 940)],
    381: [(MAIN_MAP_NAME, 896, 1060)],
    382: [(MAIN_MAP_NAME, 848, 1036)],
    383: [(MAIN_MAP_NAME, 776, 1012)],
    384: [(MAIN_MAP_NAME, 728, 1060)],
    385: [(MAIN_MAP_NAME, 704, 1084)],
    386: [(MAIN_MAP_NAME, 728, 1108)],
    387: [(MAIN_MAP_NAME, 776, 1108)],
    388: [(MAIN_MAP_NAME, 896, 1084)],
    389: [(MAIN_MAP_NAME, 872, 1108)],
    390: [(MAIN_MAP_NAME, 704, 1060)],
    391: [(MAIN_MAP_NAME, 728, 1012)],
    392: [(MAIN_MAP_NAME, 728, 988)],
    393: [(MAIN_MAP_NAME, 752, 1012)],
    394: [(MAIN_MAP_NAME, 656, 1036)],
    395: [(MAIN_MAP_NAME, 512, 1084)],
    396: [(MAIN_MAP_NAME, 536, 1060)],
    397: [(MAIN_MAP_NAME, 800, 1060)],
    398: [(MAIN_MAP_NAME, 1616, 1016)],
    399: [(MAIN_MAP_NAME, 1592, 1016)],
    400: [(MAIN_MAP_NAME, 1592, 1064)],
    401: [(MAIN_MAP_NAME, 1544, 1040)],
    402: [(MAIN_MAP_NAME, 1520, 1112)],
    403: [(MAIN_MAP_NAME, 1472, 1112)],
    404: [(MAIN_MAP_NAME, 1568, 1112)],
    405: [(MAIN_MAP_NAME, 1640, 1136)],
    406: [(MAIN_MAP_NAME, 1496, 1040)],
    407: [(MAIN_MAP_NAME, 1424, 1136)],
    408: [(MAIN_MAP_NAME, 1520, 1136)],
    409: [(MAIN_MAP_NAME, 1520, 1160)],
    410: [(MAIN_MAP_NAME, 1544, 1160)],
    411: [(MAIN_MAP_NAME, 1400, 1160)],
    412: [(MAIN_MAP_NAME, 1376, 1160)],
    413: [(MAIN_MAP_NAME, 1352, 1160)],
    414: [(MAIN_MAP_NAME, 1328, 1064)],
    415: [(MAIN_MAP_NAME, 1376, 1088)],
    416: [(MAIN_MAP_NAME, 1424, 1040)],
    417: [(MAIN_MAP_NAME, 1472, 1016)],
    418: [(MAIN_MAP_NAME, 2000, 700)],
    419: [(MAIN_MAP_NAME, 2024, 700)],
    420: [(MAIN_MAP_NAME, 1976, 800)],
    421: [(MAIN_MAP_NAME, 2192, 968)],
    422: [(MAIN_MAP_NAME, 2192, 944)],
    423: [(MAIN_MAP_NAME, 2168, 1016)],
    424: [(MAIN_MAP_NAME, 2216, 992)],
    425: [(MAIN_MAP_NAME, 2264, 992)],
    426: [(MAIN_MAP_NAME, 2288, 968)],
    427: [(MAIN_MAP_NAME, 2240, 1036)],
    428: [(MAIN_MAP_NAME, 2096, 1060)],
    429: [(MAIN_MAP_NAME, 2072, 1060)],
    430: [(MAIN_MAP_NAME, 2048, 1060)],
    431: [(MAIN_MAP_NAME, 2096, 1012)],
    432: [(MAIN_MAP_NAME, 2096, 988)],
    433: [(MAIN_MAP_NAME, 2144, 1060)],
    434: [(MAIN_MAP_NAME, 2432, 1012)],
    435: [(MAIN_MAP_NAME, 1472, 630)],
    436: [(MAIN_MAP_NAME, 1304, 580)],
    437: [(MAIN_MAP_NAME, 1352, 556)],
    438: [(MAIN_MAP_NAME, 1352, 508)],
    439: [(MAIN_MAP_NAME, 1328, 508)],
    440: [(MAIN_MAP_NAME, 1352, 484)],
    441: [(MAIN_MAP_NAME, 1304, 508)],
    442: [(MAIN_MAP_NAME, 1304, 460)],
    443: [(MAIN_MAP_NAME, 1304, 388)],
    444: [(MAIN_MAP_NAME, 1352, 340)],
    445: [(MAIN_MAP_NAME, 1352, 388)],
    446: [(MAIN_MAP_NAME, 1352, 412)],
    447: [(MAIN_MAP_NAME, 1328, 436)],
    448: [(MAIN_MAP_NAME, 1352, 460)],
    449: [(MAIN_MAP_NAME, 1424, 316)],
    450: [(MAIN_MAP_NAME, 1328, 316)],
    451: [(MAIN_MAP_NAME, 1352, 268)],
    452: [(MAIN_MAP_NAME, 1352, 292)],
    453: [(MAIN_MAP_NAME, 1400, 292)],
    454: [(MAIN_MAP_NAME, 1376, 244)],
    455: [(MAIN_MAP_NAME, 1328, 220)],
    456: [(MAIN_MAP_NAME, 1376, 196)],
    457: [(MAIN_MAP_NAME, 1352, 148)],
    458: [(MAIN_MAP_NAME, 1376, 172)],
    459: [(MAIN_MAP_NAME, 1400, 196)],
    460: [(MAIN_MAP_NAME, 1376, 100)],
    461: [(MAIN_MAP_NAME, 1400, 100)],
    462: [(MAIN_MAP_NAME, 1376, 52)],
    463: [(MAIN_MAP_NAME, 1376, 28)],
    464: [(MAIN_MAP_NAME, 1184, 702)],
    465: [(MAIN_MAP_NAME, 416, 846)],
    466: [(MAIN_MAP_NAME, 2024, 700)],
    467: [(MAIN_MAP_NAME, 2288, 820)],
    468: [(MAIN_MAP_NAME, 2120, 940)],
    469: [(MAIN_MAP_NAME, 1424, 416)],
    470: [(MAIN_MAP_NAME, 2720, 1228)],
    471: [(MAIN_MAP_NAME, 2720, 1276)],
    472: [(MAIN_MAP_NAME, 2768, 1252)],
    473: [(MAIN_MAP_NAME, 2768, 1228)],
    474: [(MAIN_MAP_NAME, 2696, 1300)],
    475: [(MAIN_MAP_NAME, 2696, 1324)],
    476: [(MAIN_MAP_NAME, 2672, 1300)],
    477: [(MAIN_MAP_NAME, 2672, 1252)],
    478: [(MAIN_MAP_NAME, 2696, 1252)],
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
    mapping_values = None
    multi_sec = False
    for k, v in map_location_mapping.items():
        if loc_name in v:
            map_locs = map_locations[k]
            mapping_values = v
            multi_sec = len(v) > 1
            break
    if map_locs is not None:
        map_locs = list(map(lambda x: PopTrackerMapLocation(*x), map_locs))
    access_rules : list[list[str]] = combine_access([[f"$has_access_to|{region}"]], get_access(data.get('requirements')), "AND")
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
