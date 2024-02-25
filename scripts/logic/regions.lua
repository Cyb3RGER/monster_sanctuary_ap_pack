REGIONS = {
  ["Menu"] = {
    ["MountainPath_North1"] = function()
      return true
    end
  },
  ["MountainPath_North1"] = {
    ["MountainPath_North2"] = function()
      return true
    end,
    ["MountainPath_North7"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["MountainPath_North2"] = {
    ["MountainPath_North1"] = function()
      return true
    end,
    ["MountainPath_North3"] = function()
      return true
    end
  },
  ["MountainPath_North3"] = {
    ["MountainPath_North2"] = function()
      return true
    end,
    ["MountainPath_North4"] = function()
      return true
    end
  },
  ["MountainPath_North4"] = {
    ["MountainPath_North3"] = function()
      return true
    end,
    ["MountainPath_North5"] = function()
      return true
    end
  },
  ["MountainPath_North5"] = {
    ["MountainPath_North4"] = function()
      return true
    end,
    ["MountainPath_NorthHidden"] = function()
      return double_jump()
    end,
    ["MountainPath_Center1"] = function()
      return true
    end,
    ["MountainPath_East1"] = function()
      return
      _OR({
        plotless(),
        keeper_rank_1()
      })
    end,
    ["BlueCave_NorthFork_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end
  },
  ["MountainPath_NorthHidden"] = {
    ["MountainPath_North5"] = function()
      return true
    end
  },
  ["MountainPath_North6"] = {
    ["MountainPath_West3"] = function()
      return true
    end,
    ["MountainPath_North7"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end
  },
  ["MountainPath_North7"] = {
    ["MountainPath_North1"] = function()
      return true
    end,
    ["MountainPath_North6"] = function()
      return true
    end
  },
  ["MountainPath_East1"] = {
    ["MountainPath_North5"] = function()
      return true
    end,
    ["KeeperStronghold_WestEntrance"] = function()
      return true
    end
  },
  ["MountainPath_Center1"] = {
    ["MountainPath_North5"] = function()
      return true
    end,
    ["MountainPath_Center2"] = function()
      return true
    end
  },
  ["MountainPath_Center2"] = {
    ["MountainPath_North1"] = function()
      return true
    end,
    ["MountainPath_Center3"] = function()
      return true
    end
  },
  ["MountainPath_Center3"] = {
    ["MountainPath_Center2"] = function()
      return true
    end,
    ["MountainPath_Center4"] = function()
      return true
    end,
    ["MountainPath_Center5"] = function()
      return true
    end,
    ["MountainPath_Center7"] = function()
      return
      _OR({
        mountain_path_key(),
        no_locked_doors()
      })
    end
  },
  ["MountainPath_Center4"] = {
    ["MountainPath_Center3"] = function()
      return true
    end
  },
  ["MountainPath_Center5"] = {
    ["MountainPath_Center3"] = function()
      return true
    end,
    ["MountainPath_West1"] = function()
      return true
    end
  },
  ["MountainPath_Center6_Lower"] = {
    ["MountainPath_West5"] = function()
      return true
    end,
    ["MountainPath_Center6_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["BlueCave_ChampionRoom2_WestAccess"] = function()
      return blue_cave_champion_room_2_west_shortcut()
    end
  },
  ["MountainPath_Center6_Upper"] = {
    ["MountainPath_Center6_Lower"] = function()
      return true
    end,
    ["MountainPath_Center7"] = function()
      return true
    end
  },
  ["MountainPath_Center7"] = {
    ["MountainPath_Center6_Upper"] = function()
      return true
    end,
    ["MountainPath_Center3"] = function()
      return true
    end
  },
  ["MountainPath_West1"] = {
    ["MountainPath_Center5"] = function()
      return true
    end,
    ["MountainPath_West2"] = function()
      return true
    end
  },
  ["MountainPath_West2"] = {
    ["MountainPath_West1"] = function()
      return true
    end,
    ["MountainPath_WestHidden"] = function()
      return breakable_walls()
    end,
    ["MountainPath_West3"] = function()
      return true
    end,
    ["MountainPath_West4"] = function()
      return true
    end,
    ["MountainPath_West5"] = function()
      return true
    end,
    ["MountainPath_SnowyEntrance"] = function()
      return true
    end,
    ["MountainPath_WestHidden2"] = function()
      return narrow_corridors()
    end
  },
  ["MountainPath_West3"] = {
    ["MountainPath_West2"] = function()
      return true
    end,
    ["MountainPath_North6"] = function()
      return true
    end
  },
  ["MountainPath_West4"] = {
    ["MountainPath_West2"] = function()
      return true
    end,
    ["MountainPath_West6"] = function()
      return true
    end
  },
  ["MountainPath_West5"] = {
    ["MountainPath_West2"] = function()
      return true
    end,
    ["MountainPath_Center6_Lower"] = function()
      return true
    end
  },
  ["MountainPath_West6"] = {
    ["MountainPath_West4"] = function()
      return true
    end
  },
  ["MountainPath_WestHidden"] = {
    ["MountainPath_West2"] = function()
      return true
    end
  },
  ["MountainPath_WestHidden2"] = {
    ["MountainPath_West2"] = function()
      return true
    end
  },
  ["MountainPath_SnowyEntrance"] = {
    ["MountainPath_West2"] = function()
      return true
    end,
    ["MountainPath_SnowyEntrance2"] = function()
      return
      _OR({
        improved_flying(),
        _AND({
          double_jump(),
          _OR({
            distant_ledges(),
            mount()
          })
        })
      })
    end
  },
  ["MountainPath_SnowyEntrance2"] = {
    ["SnowyPeaks_East1"] = function()
      return true
    end,
    ["MountainPath_SnowyEntrance"] = function()
      return
      _OR({
        improved_flying(),
        _AND({
          double_jump(),
          _OR({
            distant_ledges(),
            mount()
          })
        })
      })
    end
  },
  ["KeeperStronghold_WestEntrance"] = {
    ["MountainPath_East1"] = function()
      return true
    end,
    ["KeeperStronghold_WestStairwell"] = function()
      return true
    end
  },
  ["KeeperStronghold_WestStairwell"] = {
    ["KeeperStronghold_WestEntrance"] = function()
      return true
    end,
    ["KeeperStronghold_WestTowers"] = function()
      return true
    end,
    ["KeeperStronghold_LivingRoom1"] = function()
      return true
    end,
    ["KeeperStronghold_Shops"] = function()
      return true
    end
  },
  ["KeeperStronghold_WestTowers"] = {
    ["KeeperStronghold_WestStairwell"] = function()
      return true
    end
  },
  ["KeeperStronghold_LivingRoom1"] = {
    ["KeeperStronghold_WestStairwell"] = function()
      return true
    end
  },
  ["KeeperStronghold_Shops"] = {
    ["KeeperStronghold_WestStairwell"] = function()
      return true
    end,
    ["KeeperStronghold_CenterStairwell"] = function()
      return true
    end
  },
  ["KeeperStronghold_CenterStairwell"] = {
    ["KeeperStronghold_Shops"] = function()
      return true
    end,
    ["KeeperStronghold_LivingRoom2"] = function()
      return true
    end,
    ["KeeperStronghold_Smith"] = function()
      return true
    end,
    ["KeeperStronghold_Storage"] = function()
      return true
    end,
    ["KeeperStronghold_Library"] = function()
      return true
    end,
    ["KeeperStronghold_KeepersTowers"] = function()
      return true
    end
  },
  ["KeeperStronghold_LivingRoom2"] = {
    ["KeeperStronghold_CenterStairwell"] = function()
      return true
    end
  },
  ["KeeperStronghold_Smith"] = {
    ["KeeperStronghold_CenterStairwell"] = function()
      return true
    end
  },
  ["KeeperStronghold_Library"] = {
    ["KeeperStronghold_CenterStairwell"] = function()
      return true
    end,
    ["KeeperStronghold_EastStairwell"] = function()
      return true
    end
  },
  ["KeeperStronghold_Storage"] = {
    ["KeeperStronghold_CenterStairwell"] = function()
      return true
    end,
    ["KeeperStronghold_EastStairwell"] = function()
      return true
    end,
    ["BlueCave_StrongholdEntrance"] = function()
      return true
    end
  },
  ["KeeperStronghold_EastStairwell"] = {
    ["KeeperStronghold_Library"] = function()
      return true
    end,
    ["KeeperStronghold_Storage"] = function()
      return true
    end,
    ["KeeperStronghold_DressMaker"] = function()
      return true
    end,
    ["KeeperStronghold_ParentsRoom"] = function()
      return true
    end,
    ["StrongholdDungeon_Entrance"] = function()
      return
      _OR({
        plotless(),
        _AND({
          keeper_rank_2(),
          blue_caves_story_complete()
        })
      })
    end
  },
  ["KeeperStronghold_DressMaker"] = {
    ["KeeperStronghold_EastStairwell"] = function()
      return true
    end
  },
  ["KeeperStronghold_ParentsRoom"] = {
    ["KeeperStronghold_EastStairwell"] = function()
      return true
    end
  },
  ["KeeperStronghold_KeepersTowers"] = {
    ["KeeperStronghold_CenterStairwell"] = function()
      return true
    end,
    ["KeeperStronghold_ChampionChallenge"] = function()
      return true
    end,
    ["KeeperStronghold_DuelCircle"] = function()
      return keeper_rank_2()
    end
  },
  ["KeeperStronghold_DuelCircle"] = {
    ["KeeperStronghold_KeepersTowers"] = function()
      return true
    end
  },
  ["BlueCave_StrongholdEntrance"] = {
    ["KeeperStronghold_Storage"] = function()
      return true
    end,
    ["BlueCave_North1"] = function()
      return true
    end
  },
  ["BlueCave_North1"] = {
    ["BlueCave_StrongholdEntrance"] = function()
      return true
    end,
    ["BlueCave_Platforms"] = function()
      return true
    end,
    ["BlueCave_Switches"] = function()
      return
      _OR({
        one_blue_cave_key(),
        minimal_locked_doors(),
        no_locked_doors()
      })
    end
  },
  ["BlueCave_Switches"] = {
    ["BlueCave_North1"] = function()
      return true
    end
  },
  ["BlueCave_Platforms"] = {
    ["BlueCave_North1"] = function()
      return true
    end,
    ["BlueCave_NorthFork_Lower"] = function()
      return
      _OR({
        blue_cave_switches_access(),
        _AND({
          double_jump(),
          _OR({
            improved_flying(),
            lofty_mount(),
            dual_mobility()
          })
        })
      })
    end
  },
  ["BlueCave_NorthFork_Lower"] = {
    ["BlueCave_Platforms"] = function()
      return true
    end,
    ["BlueCave_WestStairwell"] = function()
      return true
    end,
    ["BlueCave_NorthFork_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end
  },
  ["BlueCave_NorthFork_Upper"] = {
    ["BlueCave_NorthFork_Lower"] = function()
      return true
    end,
    ["MountainPath_North5"] = function()
      return true
    end
  },
  ["BlueCave_NorthFork_West"] = {
    ["BlueCave_Chains2"] = function()
      return true
    end
  },
  ["BlueCave_WestStairwell"] = {
    ["BlueCave_NorthFork_Lower"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end,
    ["BlueCave_WestWaters1"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["BlueCave_West1"] = function()
      return true
    end,
    ["BlueCave_West2"] = function()
      return true
    end
  },
  ["BlueCave_West1"] = {
    ["BlueCave_WestStairwell"] = function()
      return true
    end,
    ["BlueCave_CentralPart"] = function()
      return true
    end
  },
  ["BlueCave_West2"] = {
    ["BlueCave_WestStairwell"] = function()
      return true
    end,
    ["BlueCave_WestHidden"] = function()
      return breakable_walls()
    end
  },
  ["BlueCave_WestHidden"] = {
    ["BlueCave_West2"] = function()
      return true
    end
  },
  ["BlueCave_CentralPart"] = {
    ["BlueCave_West1"] = function()
      return true
    end,
    ["BlueCave_East1"] = function()
      return true
    end,
    ["BlueCave_South1_Upper"] = function()
      return
      _OR({
        no_locked_doors(),
        three_blue_cave_keys(),
        _AND({
          minimal_locked_doors(),
          one_blue_cave_key()
        })
      })
    end,
    ["BlueCave_ChampionRoom"] = function()
      return
      _AND({
        _OR({
          two_blue_cave_keys(),
          minimal_locked_doors(),
          no_locked_doors()
        }),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility()
        })
      })
    end
  },
  ["BlueCave_ChampionRoom"] = {
    ["BlueCave_CentralPart"] = function()
      return true
    end,
    ["BlueCave_WestStairwell"] = function()
      return true
    end
  },
  ["BlueCave_East1"] = {
    ["BlueCave_CentralPart"] = function()
      return true
    end,
    ["BlueCave_East2_Lower"] = function()
      return true
    end
  },
  ["BlueCave_East2_Lower"] = {
    ["BlueCave_East1"] = function()
      return true
    end,
    ["BlueCave_East3"] = function()
      return true
    end,
    ["BlueCave_East2_Upper"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end
  },
  ["BlueCave_East2_Upper"] = {
    ["BlueCave_East2_Lower"] = function()
      return true
    end,
    ["BlueCave_East4"] = function()
      return true
    end,
    ["StrongholdDungeon_West4_Shortcut"] = function()
      return stronghold_dungeon_west_4_shortcut()
    end
  },
  ["BlueCave_East3"] = {
    ["BlueCave_East2_Lower"] = function()
      return true
    end
  },
  ["BlueCave_East4"] = {
    ["BlueCave_East2_Upper"] = function()
      return true
    end
  },
  ["BlueCave_South1_Upper"] = {
    ["BlueCave_CentralPart"] = function()
      return
      _OR({
        no_locked_doors(),
        three_blue_cave_keys(),
        _AND({
          minimal_locked_doors(),
          one_blue_cave_key()
        })
      })
    end,
    ["BlueCave_South1_Middle"] = function()
      return true
    end
  },
  ["BlueCave_South1_Middle"] = {
    ["BlueCave_South1_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end,
    ["BlueCave_South1_Lower"] = function()
      return true
    end,
    ["BlueCave_South7"] = function()
      return true
    end
  },
  ["BlueCave_South1_Lower"] = {
    ["BlueCave_South1_Middle"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end,
    ["BlueCave_South3"] = function()
      return true
    end,
    ["BlueCave_South4"] = function()
      return true
    end
  },
  ["BlueCave_South2"] = {
    ["BlueCave_South4"] = function()
      return true
    end
  },
  ["BlueCave_South3"] = {
    ["BlueCave_South1_Lower"] = function()
      return true
    end
  },
  ["BlueCave_South4"] = {
    ["BlueCave_South1_Lower"] = function()
      return true
    end,
    ["BlueCave_South2"] = function()
      return true
    end,
    ["BlueCave_South5"] = function()
      return true
    end,
    ["BlueCave_South6"] = function()
      return true
    end
  },
  ["BlueCave_South5"] = {
    ["BlueCave_South4"] = function()
      return true
    end,
    ["Underworld_Entrance"] = function()
      return
      _OR({
        _AND({
          plotless(),
          all_sanctuary_tokens()
        }),
        _AND({
          all_sanctuary_tokens(),
          ostanes(),
          stronghold_dungeon_library_access()
        })
      })
    end
  },
  ["BlueCave_South6"] = {
    ["BlueCave_South4"] = function()
      return true
    end
  },
  ["BlueCave_South7"] = {
    ["BlueCave_South1_Middle"] = function()
      return true
    end,
    ["BlueCave_ChampionRoom3"] = function()
      return
      _AND({
        summon_big_rock(),
        grapple()
      })
    end
  },
  ["BlueCave_ChampionRoom3"] = {
    ["BlueCave_South7"] = function()
      return true
    end
  },
  ["BlueCave_WestWaters1"] = {
    ["BlueCave_WestStairwell"] = function()
      return true
    end,
    ["BlueCave_WestStairwell2"] = function()
      return true
    end
  },
  ["BlueCave_WestStairwell2"] = {
    ["BlueCave_WestWaters1"] = function()
      return true
    end,
    ["BlueCave_WestWaters2_Upper"] = function()
      return true
    end,
    ["BlueCave_Chains1"] = function()
      return true
    end
  },
  ["BlueCave_Chains1"] = {
    ["BlueCave_WestStairwell2"] = function()
      return true
    end,
    ["BlueCave_Chains2"] = function()
      return true
    end
  },
  ["BlueCave_Chains2"] = {
    ["BlueCave_Chains1"] = function()
      return true
    end,
    ["BlueCave_NorthFork_West"] = function()
      return breakable_walls()
    end
  },
  ["BlueCave_WestWaters2_Upper"] = {
    ["BlueCave_WestWaters2_Lower"] = function()
      return true
    end,
    ["BlueCave_WestStairwell2"] = function()
      return true
    end,
    ["BlueCave_WestWaters3"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        swimming()
      })
    end
  },
  ["BlueCave_WestWaters2_Lower"] = {
    ["BlueCave_WestWaters2_Upper"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        swimming()
      })
    end,
    ["BlueCave_WestWatersHidden"] = function()
      return
      _OR({
        improved_swimming(),
        dual_mobility()
      })
    end
  },
  ["BlueCave_WestWatersHidden"] = {
    ["BlueCave_WestWaters2_Lower"] = function()
      return
      _OR({
        improved_swimming(),
        dual_mobility()
      })
    end
  },
  ["BlueCave_WestWaters3"] = {
    ["BlueCave_WestWaters2_Upper"] = function()
      return true
    end,
    ["BlueCave_WestWaters4_Middle"] = function()
      return true
    end
  },
  ["BlueCave_WestWaters4_Middle"] = {
    ["BlueCave_WestWaters3"] = function()
      return true
    end,
    ["BlueCave_WestWaters4_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["BlueCave_WestWaters4_Lower"] = function()
      return true
    end
  },
  ["BlueCave_WestWaters4_Upper"] = {
    ["BlueCave_WestWaters4_Middle"] = function()
      return true
    end,
    ["BlueCave_WestWaters7_West"] = function()
      return true
    end
  },
  ["BlueCave_WestWaters4_Lower"] = {
    ["BlueCave_WestWaters4_Middle"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end,
    ["BlueCave_WestWaters5"] = function()
      return true
    end,
    ["BlueCave_WestWaters6_Upper"] = function()
      return true
    end
  },
  ["BlueCave_WestWaters5"] = {
    ["BlueCave_WestWaters4_Lower"] = function()
      return true
    end
  },
  ["BlueCave_WestWaters6_Upper"] = {
    ["BlueCave_WestWaters4_Lower"] = function()
      return true
    end,
    ["BlueCave_WestWaters6_Lower"] = function()
      return
      _OR({
        double_jump(),
        summon_big_rock(),
        distant_ledges(),
        swimming()
      })
    end
  },
  ["BlueCave_WestWaters6_Lower"] = {
    ["BlueCave_WestWaters6_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["BlueCave_WestWatersHidden2"] = function()
      return levitate()
    end,
    ["BlueCave_AquaEntrance_Upper"] = function()
      return true
    end
  },
  ["BlueCave_WestWatersHidden2"] = {
    ["BlueCave_WestWaters6_Lower"] = function()
      return levitate()
    end
  },
  ["BlueCave_AquaEntrance_Upper"] = {
    ["BlueCave_WestWaters6_Lower"] = function()
      return true
    end,
    ["SunPalace_East1_East"] = function()
      return true
    end,
    ["BlueCave_AquaEntrance_Lower"] = function()
      return true
    end
  },
  ["BlueCave_AquaEntrance_Lower"] = {
    ["BlueCave_AquaEntrance_Upper"] = function()
      return
      _OR({
        double_jump(),
        swimming()
      })
    end
  },
  ["BlueCave_WestWaters7_East"] = {
    ["BlueCave_WestWaters4_Upper"] = function()
      return true
    end,
    ["BlueCave_WestWaters7_West"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end
  },
  ["BlueCave_WestWaters7_West"] = {
    ["BlueCave_WestWaters7_East"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["BlueCave_ChampionRoom2"] = function()
      return true
    end
  },
  ["BlueCave_ChampionRoom2"] = {
    ["BlueCave_ChampionRoom2_WestAccess"] = function()
      return true
    end,
    ["BlueCave_WestWaters7_West"] = function()
      return true
    end
  },
  ["BlueCave_ChampionRoom2_WestAccess"] = {
    ["MountainPath_Center6_Lower"] = function()
      return true
    end,
    ["BlueCave_ChampionRoom2"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Entrance"] = {
    ["KeeperStronghold_EastStairwell"] = function()
      return true
    end,
    ["StrongholdDungeon_North1"] = function()
      return true
    end,
    ["StrongholdDungeon_Jail"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Jail"] = {
    ["StrongholdDungeon_Entrance"] = function()
      return true
    end,
    ["StrongholdDungeon_JailHidden"] = function()
      return breakable_walls()
    end
  },
  ["StrongholdDungeon_JailHidden"] = {
    ["StrongholdDungeon_Jail"] = function()
      return true
    end
  },
  ["StrongholdDungeon_North1"] = {
    ["StrongholdDungeon_Entrance"] = function()
      return true
    end,
    ["StrongholdDungeon_North2"] = function()
      return true
    end
  },
  ["StrongholdDungeon_North2"] = {
    ["StrongholdDungeon_North1"] = function()
      return true
    end,
    ["StrongholdDungeon_North3"] = function()
      return true
    end,
    ["StrongholdDungeon_North6"] = function()
      return true
    end,
    ["StrongholdDungeon_Central1"] = function()
      return true
    end
  },
  ["StrongholdDungeon_North3"] = {
    ["StrongholdDungeon_North2"] = function()
      return true
    end,
    ["StrongholdDungeon_North4"] = function()
      return true
    end
  },
  ["StrongholdDungeon_North4"] = {
    ["StrongholdDungeon_North2"] = function()
      return true
    end,
    ["StrongholdDungeon_North5"] = function()
      return true
    end,
    ["MysticalWorkshop_South1"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          lofty_mount(),
          dual_mobility()
        })
      })
    end
  },
  ["StrongholdDungeon_North5"] = {
    ["StrongholdDungeon_North4"] = function()
      return true
    end,
    ["AncientWoods_West1"] = function()
      return true
    end
  },
  ["StrongholdDungeon_North6"] = {
    ["StrongholdDungeon_North2"] = function()
      return true
    end,
    ["StrongholdDungeon_West1"] = function()
      return true
    end,
    ["StrongholdDungeon_Central2"] = function()
      return true
    end,
    ["StrongholdDungeon_NorthHidden"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        summon_big_rock()
      })
    end
  },
  ["StrongholdDungeon_NorthHidden"] = {
    ["StrongholdDungeon_North6"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Central1"] = {
    ["StrongholdDungeon_Central2"] = function()
      return true
    end,
    ["StrongholdDungeon_Central3"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Central2"] = {
    ["StrongholdDungeon_North6"] = function()
      return true
    end,
    ["StrongholdDungeon_Central1"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Central3"] = {
    ["StrongholdDungeon_Central1"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["StrongholdDungeon_Central4"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Central4"] = {
    ["StrongholdDungeon_Central3"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["StrongholdDungeon_Central5_Upper"] = function()
      return true
    end,
    ["StrongholdDungeon_Central7"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Central5_Upper"] = {
    ["StrongholdDungeon_Central5_Lower"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["StrongholdDungeon_Central4"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["StrongholdDungeon_Central5_Lower"] = {
    ["StrongholdDungeon_Central5_Upper"] = function()
      return
      _OR({
        _AND({
          lightning_orbs(),
          _OR({
            double_jump(),
            distant_ledges(),
            summon_big_rock()
          })
        }),
        _AND({
          double_jump(),
          _OR({
            ground_switches(),
            improved_flying(),
            dual_mobility(),
            lofty_mount()
          })
        })
      })
    end,
    ["AncientWoods_DungeonEntrance"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Central6"] = {
    ["StrongholdDungeon_South1"] = function()
      return true
    end,
    ["StrongholdDungeon_Central7"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Central7"] = {
    ["StrongholdDungeon_Central6"] = function()
      return true
    end,
    ["StrongholdDungeon_East1_NW"] = function()
      return true
    end,
    ["StrongholdDungeon_Central4"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["StrongholdDungeon_Hidden1"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["StrongholdDungeon_CentralHidden"] = function()
      return
      _AND({
        dark_rooms(),
        double_jump()
      })
    end
  },
  ["StrongholdDungeon_CentralHidden"] = {
    ["StrongholdDungeon_Central7"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Hidden1"] = {
    ["StrongholdDungeon_Central7"] = function()
      return true
    end,
    ["StrongholdDungeon_SummonRoom"] = function()
      return summon_big_rock()
    end
  },
  ["StrongholdDungeon_SummonRoom"] = {
    ["StrongholdDungeon_Hidden1"] = function()
      return true
    end
  },
  ["StrongholdDungeon_South1"] = {
    ["StrongholdDungeon_Central6"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["StrongholdDungeon_South2"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["StrongholdDungeon_South2"] = {
    ["StrongholdDungeon_South1"] = function()
      return true
    end,
    ["StrongholdDungeon_South3"] = function()
      return true
    end
  },
  ["StrongholdDungeon_South3"] = {
    ["StrongholdDungeon_South2"] = function()
      return true
    end,
    ["StrongholdDungeon_West3"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end,
    ["StrongholdDungeon_South4"] = function()
      return
      _OR({
        no_locked_doors(),
        two_dungeon_keys(),
        _AND({
          one_dungeon_key(),
          minimal_locked_doors()
        })
      })
    end
  },
  ["StrongholdDungeon_South4"] = {
    ["StrongholdDungeon_South3"] = function()
      return
      _AND({
        _OR({
          no_locked_doors(),
          two_dungeon_keys(),
          _AND({
            one_dungeon_key(),
            minimal_locked_doors()
          })
        }),
        double_jump()
      })
    end,
    ["StrongholdDungeon_South5"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches(),
        swimming()
      })
    end
  },
  ["StrongholdDungeon_South5"] = {
    ["StrongholdDungeon_South4"] = function()
      return true
    end,
    ["StrongholdDungeon_Library"] = function()
      return true
    end
  },
  ["StrongholdDungeon_Library"] = {
    ["StrongholdDungeon_South5"] = function()
      return true
    end,
    ["StrongholdDungeon_Library2"] = function()
      return narrow_corridors()
    end
  },
  ["StrongholdDungeon_Library2"] = {
    ["StrongholdDungeon_Library"] = function()
      return narrow_corridors()
    end
  },
  ["StrongholdDungeon_West1"] = {
    ["StrongholdDungeon_North6"] = function()
      return true
    end,
    ["StrongholdDungeon_West2"] = function()
      return true
    end
  },
  ["StrongholdDungeon_West2"] = {
    ["StrongholdDungeon_West4"] = function()
      return true
    end,
    ["StrongholdDungeon_South3_Shortcut"] = function()
      return stronghold_dungeon_south_3_shortcut()
    end
  },
  ["StrongholdDungeon_West3_Shortcut"] = {
    ["StrongholdDungeon_West3"] = function()
      return true
    end,
    ["StrongholdDungeon_West2"] = function()
      return true
    end
  },
  ["StrongholdDungeon_West3"] = {
    ["StrongholdDungeon_South3"] = function()
      return true
    end,
    ["StrongholdDungeon_West3_Shortcut"] = function()
      return true
    end,
    ["StrongholdDungeon_WestHidden"] = function()
      return breakable_walls()
    end
  },
  ["StrongholdDungeon_West4"] = {
    ["StrongholdDungeon_West2"] = function()
      return true
    end,
    ["StrongholdDungeon_West4_Shortcut"] = function()
      return true
    end
  },
  ["StrongholdDungeon_West4_Shortcut"] = {
    ["StrongholdDungeon_West4"] = function()
      return true
    end,
    ["BlueCave_East2_Upper"] = function()
      return true
    end
  },
  ["StrongholdDungeon_WestHidden"] = {
    ["StrongholdDungeon_West3"] = function()
      return true
    end,
    ["StrongholdDungeon_West2_Hidden"] = function()
      return true
    end
  },
  ["StrongholdDungeon_West2_Hidden"] = {
    ["StrongholdDungeon_WestHidden"] = function()
      return true
    end,
    ["StrongholdDungeon_West4_Hidden"] = function()
      return true
    end
  },
  ["StrongholdDungeon_West4_Hidden"] = {
    ["StrongholdDungeon_West2_Hidden"] = function()
      return true
    end
  },
  ["StrongholdDungeon_East1_NW"] = {
    ["StrongholdDungeon_Central7"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["StrongholdDungeon_East1_NE"] = function()
      return
      _OR({
        one_dungeon_key(),
        minimal_locked_doors(),
        no_locked_doors()
      })
    end,
    ["StrongholdDungeon_East1_SW"] = function()
      return true
    end
  },
  ["StrongholdDungeon_East1_NE"] = {
    ["StrongholdDungeon_East5"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["StrongholdDungeon_East1_NW"] = function()
      return
      _OR({
        one_dungeon_key(),
        minimal_locked_doors(),
        no_locked_doors()
      })
    end,
    ["StrongholdDungeon_East1_SE"] = function()
      return true
    end
  },
  ["StrongholdDungeon_East1_SW"] = {
    ["StrongholdDungeon_East1_SE"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end
  },
  ["StrongholdDungeon_East1_SE"] = {
    ["StrongholdDungeon_East1_SW"] = function()
      return true
    end,
    ["StrongholdDungeon_East2"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["StrongholdDungeon_East1_NW"] = function()
      return
      _AND({
        double_jump(),
        lofty_mount()
      })
    end
  },
  ["StrongholdDungeon_East2"] = {
    ["StrongholdDungeon_East1_SE"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["StrongholdDungeon_East3"] = function()
      return true
    end,
    ["StrongholdDungeon_EastKeys"] = function()
      return true
    end
  },
  ["StrongholdDungeon_East3"] = {
    ["StrongholdDungeon_East2"] = function()
      return true
    end,
    ["StrongholdDungeon_East4"] = function()
      return true
    end,
    ["StrongholdDungeon_East5"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["StrongholdDungeon_East4"] = {
    ["StrongholdDungeon_East3"] = function()
      return true
    end,
    ["MagmaChamber_West1_West"] = function()
      return true
    end
  },
  ["StrongholdDungeon_East5"] = {
    ["StrongholdDungeon_East1_NE"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        summon_big_rock()
      })
    end,
    ["StrongholdDungeon_East3"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        summon_big_rock()
      })
    end
  },
  ["StrongholdDungeon_EastKeys"] = {
    ["StrongholdDungeon_East2"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["StrongholdDungeon_EastHidden"] = function()
      return
      _AND({
        double_jump(),
        dark_rooms()
      })
    end
  },
  ["StrongholdDungeon_EastHidden"] = {
    ["StrongholdDungeon_EastKeys"] = function()
      return true
    end
  },
  ["SnowyPeaks_East1"] = {
    ["MountainPath_SnowyEntrance2"] = function()
      return true
    end,
    ["SnowyPeaks_East2_Lower"] = function()
      return true
    end
  },
  ["SnowyPeaks_East2_Lower"] = {
    ["SnowyPeaks_East1"] = function()
      return true
    end,
    ["SnowyPeaks_East3"] = function()
      return true
    end,
    ["SnowyPeaks_East2_Upper"] = function()
      return
      _AND({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["SnowyPeaks_East2_Upper"] = {
    ["SnowyPeaks_East2_Lower"] = function()
      return true
    end,
    ["SnowyPeaks_East3"] = function()
      return breakable_walls()
    end
  },
  ["SnowyPeaks_East3"] = {
    ["SnowyPeaks_East2_Lower"] = function()
      return true
    end,
    ["SnowyPeaks_East2_Upper"] = function()
      return
      _AND({
        breakable_walls(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility(),
          lofty_mount(),
          summon_big_rock()
        })
      })
    end,
    ["SnowyPeaks_East4_Lower"] = function()
      return true
    end
  },
  ["SnowyPeaks_East4_Lower"] = {
    ["SnowyPeaks_East3"] = function()
      return true
    end,
    ["SnowyPeaks_East4_Middle"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["SnowyPeaks_East4_Middle"] = {
    ["SnowyPeaks_East5"] = function()
      return true
    end,
    ["SnowyPeaks_East4_Lower"] = function()
      return true
    end,
    ["SnowyPeaks_East4_Upper"] = function()
      return
      _AND({
        snowy_peaks_east4_upper_shortcut(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility()
        })
      })
    end
  },
  ["SnowyPeaks_East4_Upper"] = {
    ["SnowyPeaks_East4_Middle"] = function()
      return true
    end,
    ["SnowyPeaks_EastMountain2"] = function()
      return true
    end
  },
  ["SnowyPeaks_East5"] = {
    ["SnowyPeaks_East4_Middle"] = function()
      return true
    end,
    ["SnowyPeaks_West1_Upper"] = function()
      return true
    end
  },
  ["SnowyPeaks_West1_Upper"] = {
    ["SnowyPeaks_East5"] = function()
      return true
    end,
    ["SnowyPeaks_West1_Lower"] = function()
      return true
    end,
    ["SnowyPeaks_West2"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["SnowyPeaks_West1_Lower"] = {
    ["SnowyPeaks_West1_Upper"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["SnowyPeaks_SunPalaceEntrance"] = function()
      return true
    end,
    ["SnowyPeaks_WestDark"] = function()
      return breakable_walls()
    end
  },
  ["SnowyPeaks_WestDark"] = {
    ["SnowyPeaks_West1_Lower"] = function()
      return true
    end
  },
  ["SnowyPeaks_SunPalaceEntrance"] = {
    ["SnowyPeaks_West1_Lower"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        lofty_mount(),
        dual_mobility()
      })
    end,
    ["SnowyPeaks_SunPalaceEntrance_Access"] = function()
      return
      _OR({
        snowy_peaks_sun_palace_entrance_shortcut(),
        warm_underwear()
      })
    end
  },
  ["SnowyPeaks_SunPalaceEntrance_Access"] = {
    ["SnowyPeaks_SunPalaceEntrance"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        warm_underwear()
      })
    end,
    ["SunPalace_West1"] = function()
      return
      _OR({
        snowy_peaks_sun_palace_entrance_shortcut(),
        warm_underwear()
      })
    end
  },
  ["SnowyPeaks_West2"] = {
    ["SnowyPeaks_West1_Upper"] = function()
      return true
    end,
    ["SnowyPeaks_West3"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["SnowyPeaks_West3"] = {
    ["SnowyPeaks_West2"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["SnowyPeaks_West4"] = function()
      return true
    end
  },
  ["SnowyPeaks_West4"] = {
    ["SnowyPeaks_West3"] = function()
      return true
    end,
    ["SnowyPeaks_Lake_East"] = function()
      return true
    end,
    ["SnowyPeaks_WestMountain1"] = function()
      return double_jump()
    end,
    ["SnowyPeaks_West5"] = function()
      return
      _AND({
        diamond_blocks(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility()
        })
      })
    end
  },
  ["SnowyPeaks_Lake_East"] = {
    ["SnowyPeaks_West4"] = function()
      return true
    end,
    ["SnowyPeaks_Lake_Lower"] = function()
      return warm_underwear()
    end,
    ["SnowyPeaks_Lake_West"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end
  },
  ["SnowyPeaks_Lake_West"] = {
    ["SnowyPeaks_Lake_Lower"] = function()
      return warm_underwear()
    end,
    ["SnowyPeaks_Lake_East"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end
  },
  ["SnowyPeaks_Lake_Lower"] = {
    ["SnowyPeaks_Lake_West"] = function()
      return
      _OR({
        swimming(),
        _AND({
          heavy_blocks(),
          double_jump()
        })
      })
    end,
    ["SnowyPeaks_Lake_East"] = function()
      return
      _OR({
        swimming(),
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["SnowyPeaks_ChampionRoom"] = function()
      return true
    end
  },
  ["SnowyPeaks_ChampionRoom"] = {
    ["SnowyPeaks_Lake_Lower"] = function()
      return warm_underwear()
    end
  },
  ["SnowyPeaks_West5"] = {
    ["SnowyPeaks_West4"] = function()
      return diamond_blocks()
    end,
    ["SnowyPeaks_ChampionRoom2"] = function()
      return double_jump()
    end
  },
  ["SnowyPeaks_ChampionRoom2"] = {
    ["SnowyPeaks_West5"] = function()
      return true
    end
  },
  ["SnowyPeaks_WestMountain1"] = {
    ["SnowyPeaks_Cryomancer"] = function()
      return true
    end,
    ["SnowyPeaks_WestMountain2"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end
  },
  ["SnowyPeaks_Cryomancer"] = {
    ["SnowyPeaks_WestMountain1"] = function()
      return true
    end
  },
  ["SnowyPeaks_WestMountain2"] = {
    ["SnowyPeaks_WestMountain1"] = function()
      return true
    end,
    ["SnowyPeaks_WestMountain3"] = function()
      return true
    end
  },
  ["SnowyPeaks_WestMountain3"] = {
    ["SnowyPeaks_WestMountain2"] = function()
      return true
    end,
    ["SnowyPeaks_WestMountain4"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["SnowyPeaks_WestMountain6"] = function()
      return true
    end
  },
  ["SnowyPeaks_WestMountain6"] = {
    ["SnowyPeaks_WestMountain3"] = function()
      return true
    end
  },
  ["SnowyPeaks_WestMountain4"] = {
    ["SnowyPeaks_WestMountain3"] = function()
      return true
    end,
    ["SnowyPeaks_WestMountain5"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end
  },
  ["SnowyPeaks_WestMountain5"] = {
    ["SnowyPeaks_WestMountain4"] = function()
      return true
    end,
    ["SnowyPeaks_WestMountain7"] = function()
      return true
    end,
    ["SnowyPeaks_Bridge"] = function()
      return true
    end
  },
  ["SnowyPeaks_WestMountain7"] = {
    ["SnowyPeaks_WestMountain5"] = function()
      return true
    end,
    ["SnowyPeaks_WestMountainSecret"] = function()
      return double_jump()
    end
  },
  ["SnowyPeaks_WestMountainSecret"] = {
    ["SnowyPeaks_WestMountain7"] = function()
      return true
    end
  },
  ["SnowyPeaks_Bridge"] = {
    ["SnowyPeaks_EastMountain1"] = function()
      return true
    end,
    ["SnowyPeaks_WestMountain5"] = function()
      return true
    end
  },
  ["SnowyPeaks_EastMountain1"] = {
    ["SnowyPeaks_Bridge"] = function()
      return true
    end,
    ["SnowyPeaks_EastMountainTop"] = function()
      return double_jump()
    end,
    ["SnowyPeaks_ClothesmakerHouse"] = function()
      return true
    end
  },
  ["SnowyPeaks_EastMountainTop"] = {
    ["SnowyPeaks_EastMountain1"] = function()
      return true
    end
  },
  ["SnowyPeaks_ClothesmakerHouse"] = {
    ["SnowyPeaks_EastMountain1"] = function()
      return true
    end,
    ["SnowyPeaks_EastMountain4"] = function()
      return true
    end
  },
  ["SnowyPeaks_EastMountain4"] = {
    ["SnowyPeaks_ClothesmakerHouse"] = function()
      return double_jump()
    end,
    ["SnowyPeaks_EastMountain2"] = function()
      return true
    end,
    ["SnowyPeaks_EastMountain5"] = function()
      return true
    end
  },
  ["SnowyPeaks_EastMountain2"] = {
    ["SnowyPeaks_EastMountain4"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["SnowyPeaks_HighChallenge"] = function()
      return
      _AND({
        distant_ledges(),
        breakable_walls()
      })
    end,
    ["SnowyPeaks_East4_Upper"] = function()
      return true
    end
  },
  ["SnowyPeaks_EastMountain5"] = {
    ["SnowyPeaks_EastMountain4"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end,
    ["SnowyPeaks_EastMountain3_Upper"] = function()
      return true
    end
  },
  ["SnowyPeaks_HighChallenge"] = {
    ["SnowyPeaks_EastMountain2"] = function()
      return
      _AND({
        double_jump(),
        breakable_walls()
      })
    end,
    ["SnowyPeaks_EastMountain3_Shortcut"] = function()
      return true
    end
  },
  ["SnowyPeaks_EastMountain3_Shortcut"] = {
    ["SnowyPeaks_HighChallenge"] = function()
      return true
    end,
    ["SnowyPeaks_EastMountain3_Middle"] = function()
      return true
    end
  },
  ["SnowyPeaks_EastMountain3_Upper"] = {
    ["SnowyPeaks_EastMountain5"] = function()
      return true
    end,
    ["SnowyPeaks_EastMountain3_Middle"] = function()
      return true
    end
  },
  ["SnowyPeaks_EastMountain3_Middle"] = {
    ["SnowyPeaks_EastMountain3_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["SnowyPeaks_EastMountain3_Shortcut"] = function()
      return
      _AND({
        snowy_peaks_east_mountain_3_shortcut(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility()
        })
      })
    end,
    ["SnowyPeaks_EastMountain3_Lower"] = function()
      return true
    end
  },
  ["SnowyPeaks_EastMountain3_Lower"] = {
    ["SnowyPeaks_EastMountain3_Middle"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["SnowyPeaks_EastDark"] = function()
      return warm_underwear()
    end
  },
  ["SnowyPeaks_EastDark"] = {
    ["SnowyPeaks_EastMountain3_Lower"] = function()
      return warm_underwear()
    end
  },
  ["SunPalace_East1_East"] = {
    ["BlueCave_AquaEntrance_Upper"] = function()
      return true
    end,
    ["SunPalace_East1_Center"] = function()
      return lightning_orbs()
    end
  },
  ["SunPalace_East1_Center"] = {
    ["SunPalace_East1_East"] = function()
      return lightning_orbs()
    end,
    ["SunPalace_East1_West"] = function()
      return earth_orbs()
    end
  },
  ["SunPalace_East1_West"] = {
    ["SunPalace_East2"] = function()
      return true
    end,
    ["SunPalace_East1_Center"] = function()
      return earth_orbs()
    end
  },
  ["SunPalace_EastChampion"] = {
    ["SunPalace_East2"] = function()
      return true
    end
  },
  ["SunPalace_East2"] = {
    ["SunPalace_East1_West"] = function()
      return true
    end,
    ["SunPalace_East3"] = function()
      return true
    end,
    ["SunPalace_EastChampion"] = function()
      return
      _OR({
        secret_vision(),
        _AND({
          double_jump(),
          lofty_mount()
        })
      })
    end
  },
  ["SunPalace_East3"] = {
    ["SunPalace_East2"] = function()
      return true
    end,
    ["SunPalace_East4"] = function()
      return true
    end,
    ["SunPalace_East6"] = function()
      return sun_palace_east_shortcut()
    end
  },
  ["SunPalace_East4"] = {
    ["SunPalace_East3"] = function()
      return true
    end,
    ["SunPalace_Center"] = function()
      return true
    end
  },
  ["SunPalace_East5"] = {
    ["SunPalace_EastSewers5"] = function()
      return true
    end,
    ["SunPalace_East6"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["SunPalace_East6"] = {
    ["SunPalace_East5"] = function()
      return true
    end,
    ["SunPalace_East3"] = function()
      return true
    end
  },
  ["SunPalace_Center"] = {
    ["SunPalace_East4"] = function()
      return true
    end,
    ["SunPalace_West3"] = function()
      return true
    end,
    ["SunPalace_South1_Upper"] = function()
      return true
    end,
    ["SunPalace_North1"] = function()
      return
      _AND({
        sun_palace_raise_center_3(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility(),
          lofty_mount(),
          summon_big_rock()
        })
      })
    end,
    ["SunPalace_North3"] = function()
      return
      _AND({
        sun_palace_raise_center_3(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility(),
          lofty_mount(),
          summon_big_rock()
        })
      })
    end
  },
  ["SunPalace_West2"] = {
    ["SunPalace_West1"] = function()
      return true
    end,
    ["SunPalace_West3"] = function()
      return true
    end,
    ["SunPalace_West5"] = function()
      return sun_palace_west_shortcut()
    end
  },
  ["SunPalace_West1"] = {
    ["SunPalace_West2"] = function()
      return true
    end,
    ["SnowyPeaks_SunPalaceEntrance_Access"] = function()
      return true
    end
  },
  ["SunPalace_West3"] = {
    ["SunPalace_West2"] = function()
      return true
    end,
    ["SunPalace_Center"] = function()
      return true
    end
  },
  ["SunPalace_West4"] = {
    ["SunPalace_West5"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["SunPalace_WestSewers2"] = function()
      return true
    end
  },
  ["SunPalace_West5"] = {
    ["SunPalace_West2"] = function()
      return true
    end,
    ["SunPalace_West4"] = function()
      return true
    end
  },
  ["SunPalace_South1_Upper"] = {
    ["SunPalace_Center"] = function()
      return
      _OR({
        sun_palace_lower_water_1(),
        _AND({
          _NOT(sun_palace_lower_water_1()),
          _OR({
            swimming(),
            double_jump(),
            improved_flying(),
            dual_mobility(),
            summon_big_rock()
          })
        })
      })
    end,
    ["SunPalace_South2"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["SunPalace_South1_Lower"] = function()
      return
      _OR({
        _AND({
          swimming(),
          _NOT(sun_palace_lower_water_1())
        }),
        _AND({
          sun_palace_lower_water_1(),
          _OR({
            double_jump(),
            improved_flying(),
            dual_mobility()
          })
        })
      })
    end
  },
  ["SunPalace_South1_Lower"] = {
    ["SunPalace_South1_Upper"] = function()
      return
      _OR({
        _AND({
          _NOT(sun_palace_lower_water_1()),
          swimming()
        }),
        _AND({
          sun_palace_lower_water_1(),
          double_jump()
        })
      })
    end,
    ["SunPalace_EastSewers1"] = function()
      return
      _OR({
        _AND({
          _NOT(sun_palace_lower_water_2()),
          swimming()
        }),
        sun_palace_lower_water_2(),
        double_jump()
      })
    end,
    ["SunPalace_WestSewers1"] = function()
      return
      _OR({
        _AND({
          _NOT(sun_palace_lower_water_2()),
          swimming()
        }),
        _AND({
          sun_palace_lower_water_2(),
          _OR({
            double_jump(),
            improved_flying(),
            dual_mobility()
          })
        })
      })
    end
  },
  ["SunPalace_South2"] = {
    ["SunPalace_South1_Upper"] = function()
      return true
    end,
    ["SunPalace_South3"] = function()
      return true
    end
  },
  ["SunPalace_South3"] = {
    ["SunPalace_South2"] = function()
      return true
    end,
    ["SunPalace_South4"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["SunPalace_South4"] = {
    ["SunPalace_South2"] = function()
      return true
    end,
    ["SunPalace_South3"] = function()
      return true
    end
  },
  ["SunPalace_EastSewers1"] = {
    ["SunPalace_South1_Lower"] = function()
      return true
    end,
    ["SunPalace_EastSewers2"] = function()
      return true
    end
  },
  ["SunPalace_EastSewers2"] = {
    ["SunPalace_EastSewers1"] = function()
      return true
    end,
    ["SunPalace_EastSewers3"] = function()
      return true
    end,
    ["SunPalace_EastSewers6"] = function()
      return true
    end
  },
  ["SunPalace_EastSewers3"] = {
    ["SunPalace_EastSewers2"] = function()
      return true
    end,
    ["SunPalace_EastSewers4"] = function()
      return true
    end
  },
  ["SunPalace_EastSewers4"] = {
    ["SunPalace_EastSewers3"] = function()
      return true
    end,
    ["SunPalace_EastSewers5"] = function()
      return true
    end
  },
  ["SunPalace_EastSewers5"] = {
    ["SunPalace_EastSewers4"] = function()
      return true
    end,
    ["SunPalace_East5"] = function()
      return true
    end
  },
  ["SunPalace_EastSewers6"] = {
    ["SunPalace_EastSewers2"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["Underworld_West1"] = function()
      return underworld_to_sun_palace_shortcut()
    end
  },
  ["SunPalace_WestSewers1"] = {
    ["SunPalace_South1_Lower"] = function()
      return true
    end,
    ["SunPalace_WestSewers3"] = function()
      return true
    end,
    ["SunPalace_WestSewers4"] = function()
      return true
    end
  },
  ["SunPalace_WestSewers2"] = {
    ["SunPalace_WestSewers3"] = function()
      return true
    end,
    ["SunPalace_West4"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end,
    ["SunPalace_WestSewersSecret"] = function()
      return breakable_walls()
    end,
    ["SunPalace_WestSewersSecret2"] = function()
      return
      _AND({
        grapple(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility(),
          lofty_mount(),
          summon_big_rock()
        })
      })
    end
  },
  ["SunPalace_WestSewers3"] = {
    ["SunPalace_WestSewers1"] = function()
      return true
    end,
    ["SunPalace_WestSewers2"] = function()
      return
      _OR({
        double_jump(),
        swimming()
      })
    end
  },
  ["SunPalace_WestSewers4"] = {
    ["SunPalace_WestSewers1"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end
  },
  ["SunPalace_WestSewersSecret"] = {
    ["SunPalace_WestSewers2"] = function()
      return true
    end
  },
  ["SunPalace_WestSewersSecret2"] = {
    ["SunPalace_WestSewers2"] = function()
      return true
    end
  },
  ["SunPalace_North1"] = {
    ["SunPalace_North2"] = function()
      return true
    end,
    ["SunPalace_Center"] = function()
      return true
    end
  },
  ["SunPalace_North2"] = {
    ["SunPalace_North1"] = function()
      return true
    end
  },
  ["SunPalace_North3"] = {
    ["SunPalace_Center"] = function()
      return true
    end
  },
  ["AncientWoods_West1"] = {
    ["StrongholdDungeon_North5"] = function()
      return true
    end,
    ["AncientWoods_West2_Upper"] = function()
      return true
    end
  },
  ["AncientWoods_West2_Upper"] = {
    ["AncientWoods_West1"] = function()
      return true
    end,
    ["AncientWoods_West3"] = function()
      return true
    end,
    ["AncientWoods_West2_Lower"] = function()
      return true
    end
  },
  ["AncientWoods_West2_Lower"] = {
    ["AncientWoods_West2_Upper"] = function()
      return
      _OR({
        double_jump(),
        summon_big_rock(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["AncientWoods_West4"] = function()
      return true
    end,
    ["AncientWoods_WestJumpPuzzle"] = function()
      return true
    end
  },
  ["AncientWoods_West3"] = {
    ["AncientWoods_West2_Upper"] = function()
      return true
    end
  },
  ["AncientWoods_West4"] = {
    ["AncientWoods_West2_Lower"] = function()
      return true
    end,
    ["AncientWoods_West5"] = function()
      return true
    end
  },
  ["AncientWoods_West5"] = {
    ["AncientWoods_West4"] = function()
      return true
    end,
    ["AncientWoods_Center4"] = function()
      return true
    end
  },
  ["AncientWoods_West6"] = {
    ["AncientWoods_Center4"] = function()
      return double_jump()
    end,
    ["AncientWoods_WestHidden2"] = function()
      return
      _AND({
        impassible_vines(),
        breakable_walls()
      })
    end,
    ["AncientWoods_West7"] = function()
      return
      _AND({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["AncientWoods_West7"] = {
    ["AncientWoods_West6"] = function()
      return
      _OR({
        impassible_vines(),
        _AND({
          double_jump(),
          distant_ledges()
        })
      })
    end,
    ["AncientWoods_WestDescent_Upper"] = function()
      return
      _OR({
        impassible_vines(),
        _AND({
          double_jump(),
          distant_ledges()
        })
      })
    end
  },
  ["AncientWoods_WestJumpPuzzle"] = {
    ["AncientWoods_West2_Lower"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["AncientWoods_WestHidden"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["AncientWoods_WestHidden"] = {
    ["AncientWoods_WestJumpPuzzle"] = function()
      return true
    end
  },
  ["AncientWoods_WestHidden2"] = {
    ["AncientWoods_West6"] = function()
      return true
    end
  },
  ["AncientWoods_WestDescent_Upper"] = {
    ["AncientWoods_West7"] = function()
      return true
    end
  },
  ["AncientWoods_WestDescent_Middle"] = {
    ["AncientWoods_WestDescent_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["AncientWoods_WestDescent_Lower"] = function()
      return true
    end,
    ["AncientWoods_SouthHidden1"] = function()
      return breakable_walls()
    end
  },
  ["AncientWoods_WestDescent_Lower"] = {
    ["AncientWoods_WestDescent_Middle"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["AncientWoods_WestDescent2"] = function()
      return true
    end,
    ["AncientWoods_WestDescent3"] = function()
      return true
    end
  },
  ["AncientWoods_WestDescent2"] = {
    ["AncientWoods_WestDescent_Lower"] = function()
      return true
    end,
    ["StrongholdDungeon_East4"] = function()
      return true
    end
  },
  ["AncientWoods_WestDescent3"] = {
    ["AncientWoods_WestDescent_Lower"] = function()
      return true
    end,
    ["AncientWoods_DarkRoom2"] = function()
      return true
    end,
    ["AncientWoods_DungeonEntrance"] = function()
      return double_jump()
    end
  },
  ["AncientWoods_DungeonEntrance"] = {
    ["AncientWoods_WestDescent3"] = function()
      return true
    end,
    ["StrongholdDungeon_Central5"] = function()
      return true
    end
  },
  ["AncientWoods_DarkRoom2"] = {
    ["AncientWoods_WestDescent3"] = function()
      return true
    end
  },
  ["AncientWoods_Center1"] = {
    ["AncientWoods_Center2"] = function()
      return true
    end,
    ["AncientWoods_Center3"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end,
    ["AncientWoods_Center4"] = function()
      return true
    end
  },
  ["AncientWoods_Center2"] = {
    ["AncientWoods_Center1"] = function()
      return true
    end,
    ["AncientWoods_Center5"] = function()
      return
      _OR({
        two_ancient_woods_keys(),
        no_locked_doors()
      })
    end
  },
  ["AncientWoods_Center3"] = {
    ["AncientWoods_Center1"] = function()
      return true
    end,
    ["AncientWoods_TreeOfEvolution"] = function()
      return true
    end
  },
  ["AncientWoods_Center4"] = {
    ["AncientWoods_West5"] = function()
      return true
    end,
    ["AncientWoods_West6"] = function()
      return true
    end,
    ["AncientWoods_Center1"] = function()
      return true
    end,
    ["AncientWoods_DoorPuzzle"] = function()
      return true
    end
  },
  ["AncientWoods_Center5"] = {
    ["AncientWoods_Center2"] = function()
      return
      _OR({
        two_ancient_woods_keys(),
        no_locked_doors()
      })
    end,
    ["AncientWoods_Center6"] = function()
      return true
    end
  },
  ["AncientWoods_Center6"] = {
    ["AncientWoods_Center5"] = function()
      return true
    end,
    ["AncientWoods_Center7"] = function()
      return true
    end,
    ["AncientWoods_North1"] = function()
      return true
    end
  },
  ["AncientWoods_Center7"] = {
    ["AncientWoods_Center6"] = function()
      return true
    end,
    ["AncientWoods_East1"] = function()
      return true
    end,
    ["AncientWoods_South1"] = function()
      return true
    end
  },
  ["AncientWoods_North1"] = {
    ["AncientWoods_Center6"] = function()
      return true
    end,
    ["AncientWoods_North4"] = function()
      return true
    end,
    ["AncientWoods_North2"] = function()
      return true
    end
  },
  ["AncientWoods_North2"] = {
    ["AncientWoods_North1"] = function()
      return true
    end,
    ["AncientWoods_North3"] = function()
      return
      _OR({
        three_ancient_woods_keys(),
        minimal_locked_doors(),
        no_locked_doors()
      })
    end
  },
  ["AncientWoods_North3"] = {
    ["AncientWoods_North2"] = function()
      return true
    end,
    ["AncientWoods_East1_Shortcut"] = function()
      return true
    end
  },
  ["AncientWoods_North4"] = {
    ["AncientWoods_North1"] = function()
      return true
    end,
    ["AncientWoods_North5"] = function()
      return true
    end
  },
  ["AncientWoods_North5"] = {
    ["AncientWoods_North4"] = function()
      return true
    end
  },
  ["AncientWoods_East1_Shortcut"] = {
    ["AncientWoods_East1"] = function()
      return true
    end,
    ["AncientWoods_North3"] = function()
      return true
    end
  },
  ["AncientWoods_East1"] = {
    ["AncientWoods_East1_Shortcut"] = function()
      return ancient_woods_east_shortcut()
    end,
    ["AncientWoods_Center7"] = function()
      return true
    end,
    ["AncientWoods_East2_West"] = function()
      return true
    end
  },
  ["AncientWoods_East2_West"] = {
    ["AncientWoods_East1"] = function()
      return true
    end,
    ["AncientWoods_East2_East"] = function()
      return ancient_woods_beach_access()
    end
  },
  ["AncientWoods_East2_East"] = {
    ["AncientWoods_East2_West"] = function()
      return ancient_woods_beach_access()
    end,
    ["AncientWoods_East3"] = function()
      return true
    end
  },
  ["AncientWoods_East3"] = {
    ["AncientWoods_East2_East"] = function()
      return ancient_woods_beach_access()
    end,
    ["AncientWoods_East4"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end,
    ["HorizonBeach_Farm"] = function()
      return true
    end
  },
  ["AncientWoods_East4"] = {
    ["AncientWoods_East3"] = function()
      return true
    end
  },
  ["AncientWoods_South1"] = {
    ["AncientWoods_Center7"] = function()
      return true
    end,
    ["AncientWoods_South2"] = function()
      return true
    end,
    ["AncientWoods_DarkRoom"] = function()
      return true
    end,
    ["AncientWoods_South1_Lower"] = function()
      return true
    end
  },
  ["AncientWoods_South1_Lower"] = {
    ["AncientWoods_South1"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["MagmaChamber_North5_Upper"] = function()
      return ancient_woods_magma_chamber_shortcut()
    end
  },
  ["AncientWoods_South2"] = {
    ["AncientWoods_South1"] = function()
      return true
    end,
    ["AncientWoods_South3"] = function()
      return true
    end,
    ["AncientWoods_TorchesRoom"] = function()
      return true
    end,
    ["AncientWoods_South4"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end
  },
  ["AncientWoods_South3"] = {
    ["AncientWoods_South2"] = function()
      return true
    end
  },
  ["AncientWoods_South4"] = {
    ["AncientWoods_South3"] = function()
      return true
    end,
    ["AncientWoods_SouthHidden2"] = function()
      return true
    end
  },
  ["AncientWoods_DarkRoom"] = {
    ["AncientWoods_South1"] = function()
      return true
    end
  },
  ["AncientWoods_TorchesRoom"] = {
    ["AncientWoods_South2"] = function()
      return true
    end
  },
  ["AncientWoods_SouthHidden1_West"] = {
    ["AncientWoods_WestDescent_Middle"] = function()
      return true
    end,
    ["AncientWoods_SouthHidden1_East"] = function()
      return
      _AND({
        _OR({
          torches(),
          dark_rooms()
        }),
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end
  },
  ["AncientWoods_SouthHidden1_East"] = {
    ["AncientWoods_SouthHidden2"] = function()
      return true
    end,
    ["AncientWoods_SouthHidden1_West"] = function()
      return true
    end
  },
  ["AncientWoods_SouthHidden2"] = {
    ["AncientWoods_SouthHidden1_East"] = function()
      return
      _AND({
        dark_rooms(),
        double_jump()
      })
    end,
    ["AncientWoods_SouthHidden3"] = function()
      return
      _AND({
        dark_rooms(),
        double_jump()
      })
    end
  },
  ["AncientWoods_SouthHidden3"] = {
    ["AncientWoods_SouthHidden2"] = function()
      return
      _AND({
        dark_rooms(),
        double_jump()
      })
    end,
    ["AncientWoods_SouthChampion"] = function()
      return
      _AND({
        dark_rooms(),
        double_jump()
      })
    end
  },
  ["AncientWoods_SouthHidden4"] = {
    ["AncientWoods_South4"] = function()
      return
      _AND({
        dark_rooms(),
        double_jump()
      })
    end,
    ["AncientWoods_SouthChampion"] = function()
      return
      _AND({
        dark_rooms(),
        double_jump()
      })
    end
  },
  ["AncientWoods_SouthChampion"] = {
    ["AncientWoods_SouthHidden3"] = function()
      return true
    end,
    ["AncientWoods_SouthHidden4"] = function()
      return true
    end
  },
  ["AncientWoods_TreeOfEvolution"] = {
    ["AncientWoods_Center3"] = function()
      return true
    end
  },
  ["AncientWoods_DoorPuzzle"] = {
    ["AncientWoods_Center4"] = function()
      return true
    end
  },
  ["HorizonBeach_Farm"] = {
    ["AncientWoods_East3"] = function()
      return true
    end,
    ["HorizonBeach_West1"] = function()
      return true
    end
  },
  ["HorizonBeach_West1"] = {
    ["HorizonBeach_Farm"] = function()
      return true
    end,
    ["HorizonBeach_West2_Entrance"] = function()
      return swimming()
    end
  },
  ["HorizonBeach_West2_Entrance"] = {
    ["HorizonBeach_West1"] = function()
      return true
    end,
    ["HorizonBeach_West2"] = function()
      return
      _OR({
        plotless(),
        goblin_king_defeated()
      })
    end
  },
  ["HorizonBeach_West2"] = {
    ["HorizonBeach_West2_Entrance"] = function()
      return true
    end,
    ["HorizonBeach_West3"] = function()
      return true
    end
  },
  ["HorizonBeach_West3"] = {
    ["HorizonBeach_West2"] = function()
      return true
    end,
    ["HorizonBeach_West4"] = function()
      return true
    end
  },
  ["HorizonBeach_West4"] = {
    ["HorizonBeach_West3"] = function()
      return
      _OR({
        double_jump(),
        swimming(),
        distant_ledges()
      })
    end,
    ["HorizonBeach_West5"] = function()
      return true
    end
  },
  ["HorizonBeach_West5"] = {
    ["HorizonBeach_West4"] = function()
      return true
    end,
    ["HorizonBeach_Center1"] = function()
      return true
    end
  },
  ["HorizonBeach_Center1"] = {
    ["HorizonBeach_West5"] = function()
      return
      _OR({
        double_jump(),
        swimming()
      })
    end,
    ["HorizonBeach_Center2_Shortcut"] = function()
      return
      _AND({
        swimming(),
        horizon_beach_center_shortcut()
      })
    end,
    ["HorizonBeach_Labyrinth"] = function()
      return true
    end
  },
  ["HorizonBeach_Center2"] = {
    ["HorizonBeach_Center2_Shortcut"] = function()
      return true
    end,
    ["HorizonBeach_Center3"] = function()
      return true
    end
  },
  ["HorizonBeach_Center2_Shortcut"] = {
    ["HorizonBeach_Center2"] = function()
      return true
    end,
    ["HorizonBeach_Center1"] = function()
      return horizon_beach_center_shortcut()
    end
  },
  ["HorizonBeach_Center3"] = {
    ["HorizonBeach_Labyrinth"] = function()
      return swimming()
    end,
    ["HorizonBeach_Center2"] = function()
      return swimming()
    end,
    ["HorizonBeach_Center4"] = function()
      return true
    end
  },
  ["HorizonBeach_Center4"] = {
    ["HorizonBeach_Center3"] = function()
      return swimming()
    end,
    ["HorizonBeach_Center5"] = function()
      return swimming()
    end,
    ["HorizonBeach_Center6"] = function()
      return swimming()
    end
  },
  ["HorizonBeach_Center5"] = {
    ["HorizonBeach_Center4"] = function()
      return swimming()
    end,
    ["HorizonBeach_FWExit"] = function()
      return forgotten_world_to_horizon_beach_shortcut()
    end
  },
  ["HorizonBeach_Center6"] = {
    ["HorizonBeach_Center4"] = function()
      return true
    end,
    ["HorizonBeach_East1"] = function()
      return swimming()
    end,
    ["HorizonBeach_East3"] = function()
      return improved_swimming()
    end
  },
  ["HorizonBeach_East1"] = {
    ["HorizonBeach_Center6"] = function()
      return true
    end,
    ["HorizonBeach_East2_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["HorizonBeach_East2_Upper"] = {
    ["HorizonBeach_East1"] = function()
      return true
    end,
    ["HorizonBeach_East6"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["HorizonBeach_East4"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["HorizonBeach_East2_Middle"] = function()
      return true
    end
  },
  ["HorizonBeach_East2_Middle"] = {
    ["HorizonBeach_Fisher"] = function()
      return true
    end,
    ["HorizonBeach_East2_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["HorizonBeach_East2_Lower"] = function()
      return true
    end
  },
  ["HorizonBeach_East2_Lower"] = {
    ["HorizonBeach_East3"] = function()
      return true
    end,
    ["HorizonBeach_EastHidden"] = function()
      return narrow_corridors()
    end,
    ["HorizonBeach_East2_Middle"] = function()
      return swimming()
    end
  },
  ["HorizonBeach_East3"] = {
    ["HorizonBeach_East2"] = function()
      return improved_swimming()
    end,
    ["HorizonBeach_Center6"] = function()
      return true
    end
  },
  ["HorizonBeach_East4"] = {
    ["HorizonBeach_East2_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["HorizonBeach_East5"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["HorizonBeach_East5"] = {
    ["HorizonBeach_East4"] = function()
      return true
    end
  },
  ["HorizonBeach_East6"] = {
    ["HorizonBeach_East2_Upper"] = function()
      return true
    end
  },
  ["HorizonBeach_Fisher"] = {
    ["HorizonBeach_East2_Middle"] = function()
      return true
    end
  },
  ["HorizonBeach_EastHidden"] = {
    ["HorizonBeach_East2_Lower"] = function()
      return
      _AND({
        narrow_corridors(),
        double_jump()
      })
    end,
    ["HorizonBeach_EastChampion"] = function()
      return narrow_corridors()
    end
  },
  ["HorizonBeach_EastChampion"] = {
    ["HorizonBeach_EastHidden"] = function()
      return true
    end
  },
  ["HorizonBeach_Labyrinth"] = {
    ["HorizonBeach_Center1"] = function()
      return swimming()
    end,
    ["HorizonBeach_Center3"] = function()
      return swimming()
    end,
    ["HorizonBeach_South1"] = function()
      return swimming()
    end
  },
  ["HorizonBeach_South1"] = {
    ["HorizonBeach_Labyrinth"] = function()
      return true
    end,
    ["HorizonBeach_South2"] = function()
      return true
    end
  },
  ["HorizonBeach_South2"] = {
    ["HorizonBeach_South1"] = function()
      return swimming()
    end,
    ["HorizonBeach_South3"] = function()
      return swimming()
    end,
    ["HorizonBeach_South6"] = function()
      return swimming()
    end,
    ["HorizonBeach_TreasureCaveEntrance"] = function()
      return swimming()
    end
  },
  ["HorizonBeach_South3"] = {
    ["HorizonBeach_South2"] = function()
      return swimming()
    end,
    ["HorizonBeach_South4"] = function()
      return swimming()
    end
  },
  ["HorizonBeach_South4"] = {
    ["HorizonBeach_South3"] = function()
      return true
    end,
    ["HorizonBeach_South5"] = function()
      return swimming()
    end
  },
  ["HorizonBeach_South5"] = {
    ["HorizonBeach_South4"] = function()
      return swimming()
    end,
    ["HorizonBeach_Pit"] = function()
      return swimming()
    end
  },
  ["HorizonBeach_South6"] = {
    ["HorizonBeach_South5"] = function()
      return swimming()
    end
  },
  ["HorizonBeach_Pit"] = {
    ["HorizonBeach_South5"] = function()
      return true
    end
  },
  ["HorizonBeach_Pit_Secret"] = {
    ["HorizonBeach_TreasureCave4"] = function()
      return true
    end
  },
  ["HorizonBeach_TreasureCaveEntrance"] = {
    ["HorizonBeach_South2"] = function()
      return true
    end,
    ["HorizonBeach_TreasureCave1"] = function()
      return
      _OR({
        plotless(),
        horizon_beach_rescue_leonard()
      })
    end
  },
  ["HorizonBeach_TreasureCave1"] = {
    ["HorizonBeach_TreasureCaveEntrance"] = function()
      return true
    end,
    ["HorizonBeach_TreasureCave2"] = function()
      return true
    end
  },
  ["HorizonBeach_TreasureCave2"] = {
    ["HorizonBeach_TreasureCave1"] = function()
      return swimming()
    end,
    ["HorizonBeach_TreasureCave3"] = function()
      return true
    end,
    ["HorizonBeach_TreasureCave4"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end,
    ["HorizonBeach_TreasureCave5"] = function()
      return swimming()
    end,
    ["HorizonBeach_FWEntrance1"] = function()
      return true
    end
  },
  ["HorizonBeach_TreasureCave3"] = {
    ["HorizonBeach_TreasureCave2"] = function()
      return true
    end
  },
  ["HorizonBeach_TreasureCave4"] = {
    ["HorizonBeach_TreasureCave2"] = function()
      return true
    end,
    ["HorizonBeach_Pit_Secret"] = function()
      return true
    end
  },
  ["HorizonBeach_TreasureCave5"] = {
    ["HorizonBeach_TreasureCave2"] = function()
      return true
    end,
    ["HorizonBeach_Champion"] = function()
      return true
    end
  },
  ["HorizonBeach_Champion"] = {
    ["HorizonBeach_TreasureCave5"] = function()
      return true
    end,
    ["MagmaChamber_East3_Lower"] = function()
      return true
    end
  },
  ["HorizonBeach_FWEntrance1"] = {
    ["HorizonBeach_TreasureCave2"] = function()
      return true
    end,
    ["HorizonBeach_FWEntrance2"] = function()
      return true
    end
  },
  ["HorizonBeach_FWEntrance2"] = {
    ["HorizonBeach_FWEntrance1"] = function()
      return
      _OR({
        secret_vision(),
        _AND({
          double_jump(),
          lofty_mount()
        })
      })
    end,
    ["HorizonBeach_FWEntrance3"] = function()
      return
      _OR({
        secret_vision(),
        _AND({
          double_jump(),
          lofty_mount()
        })
      })
    end
  },
  ["HorizonBeach_FWEntrance3"] = {
    ["HorizonBeach_FWEntrance2"] = function()
      return true
    end,
    ["HorizonBeach_FWEntrance4"] = function()
      return true
    end
  },
  ["HorizonBeach_FWEntrance4"] = {
    ["HorizonBeach_FWEntrance3"] = function()
      return true
    end,
    ["ForgottenWorld_Fall1"] = function()
      return true
    end
  },
  ["HorizonBeach_FWExit"] = {
    ["HorizonBeach_Center5"] = function()
      return forgotten_world_to_horizon_beach_shortcut()
    end,
    ["ForgottenWorld_Climb5"] = function()
      return true
    end
  },
  ["MagmaChamber_West1_West"] = {
    ["StrongholdDungeon_East4"] = function()
      return true
    end,
    ["MagmaChamber_West1_East"] = function()
      return mount()
    end
  },
  ["MagmaChamber_West1_East"] = {
    ["MagmaChamber_West1_West"] = function()
      return mount()
    end,
    ["MagmaChamber_West6_Upper"] = function()
      return true
    end
  },
  ["MagmaChamber_West2"] = {
    ["MagmaChamber_West6_Upper"] = function()
      return true
    end,
    ["MagmaChamber_West3"] = function()
      return true
    end
  },
  ["MagmaChamber_West3"] = {
    ["MagmaChamber_West2"] = function()
      return true
    end,
    ["MagmaChamber_West4_Lower"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end,
    ["MagmaChamber_Center1"] = function()
      return true
    end
  },
  ["MagmaChamber_West4_Lower"] = {
    ["MagmaChamber_West3"] = function()
      return true
    end,
    ["MagmaChamber_West4_Ledge"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["MagmaChamber_West4_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end
  },
  ["MagmaChamber_West4_Ledge"] = {
    ["MagmaChamber_West4_Lower"] = function()
      return true
    end
  },
  ["MagmaChamber_West4_Upper"] = {
    ["MagmaChamber_West4_Lower"] = function()
      return true
    end,
    ["MagmaChamber_West5"] = function()
      return true
    end
  },
  ["MagmaChamber_West5"] = {
    ["MagmaChamber_West4_Upper"] = function()
      return true
    end,
    ["MagmaChamber_North2"] = function()
      return true
    end
  },
  ["MagmaChamber_West6_Upper"] = {
    ["MagmaChamber_West1_East"] = function()
      return true
    end,
    ["MagmaChamber_West6_Lower"] = function()
      return true
    end,
    ["MagmaChamber_West2"] = function()
      return true
    end
  },
  ["MagmaChamber_West6_Lower"] = {
    ["MagmaChamber_West6_Upper"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end,
    ["MagmaChamber_West7"] = function()
      return true
    end
  },
  ["MagmaChamber_West7"] = {
    ["MagmaChamber_West6_Lower"] = function()
      return true
    end,
    ["BlobBurg_East1"] = function()
      return all_blob_keys_used()
    end
  },
  ["MagmaChamber_North1"] = {
    ["MagmaChamber_North2"] = function()
      return true
    end,
    ["MagmaChamber_North3"] = function()
      return true
    end
  },
  ["MagmaChamber_North2"] = {
    ["MagmaChamber_North1"] = function()
      return true
    end,
    ["MagmaChamber_North5_Lower"] = function()
      return true
    end
  },
  ["MagmaChamber_North3"] = {
    ["MagmaChamber_North1"] = function()
      return true
    end,
    ["MagmaChamber_North5"] = function()
      return true
    end,
    ["MagmaChamber_North8_East"] = function()
      return true
    end
  },
  ["MagmaChamber_North4"] = {
    ["MagmaChamber_North5_Lower"] = function()
      return true
    end,
    ["MagmaChamber_Runestone"] = function()
      return true
    end
  },
  ["MagmaChamber_North5_Lower"] = {
    ["MagmaChamber_North5_Upper"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end,
    ["MagmaChamber_North2"] = function()
      return true
    end,
    ["MagmaChamber_North4"] = function()
      return true
    end,
    ["MagmaChamber_North7"] = function()
      return true
    end
  },
  ["MagmaChamber_North5_Upper"] = {
    ["MagmaChamber_North5_Lower"] = function()
      return true
    end,
    ["AncientWoods_South1_Lower"] = function()
      return ancient_woods_magma_chamber_shortcut()
    end
  },
  ["MagmaChamber_North6"] = {
    ["MagmaChamber_Runestone"] = function()
      return true
    end,
    ["MagmaChamber_East1"] = function()
      return true
    end
  },
  ["MagmaChamber_North7"] = {
    ["MagmaChamber_North5_Lower"] = function()
      return true
    end
  },
  ["MagmaChamber_North8_East"] = {
    ["MagmaChamber_North3"] = function()
      return true
    end,
    ["MagmaChamber_North8_West"] = function()
      return magma_chamber_north_shortcut()
    end
  },
  ["MagmaChamber_North8_West"] = {
    ["MagmaChamber_Center7"] = function()
      return true
    end,
    ["MagmaChamber_North8_East"] = function()
      return magma_chamber_north_shortcut()
    end
  },
  ["MagmaChamber_Runestone"] = {
    ["MagmaChamber_North4"] = function()
      return true
    end,
    ["MagmaChamber_North6"] = function()
      return true
    end
  },
  ["MagmaChamber_East1"] = {
    ["MagmaChamber_East2"] = function()
      return true
    end,
    ["MagmaChamber_North6"] = function()
      return true
    end,
    ["MagmaChamber_Center9_Upper"] = function()
      return magma_chamber_east_shortcut()
    end
  },
  ["MagmaChamber_East2"] = {
    ["MagmaChamber_East1"] = function()
      return true
    end,
    ["MagmaChamber_East3"] = function()
      return horizon_beach_to_magma_chamber_shortcut()
    end
  },
  ["MagmaChamber_East3_Upper"] = {
    ["MagmaChamber_East2"] = function()
      return horizon_beach_to_magma_chamber_shortcut()
    end,
    ["MagmaChamber_East3_Lower"] = function()
      return true
    end,
    ["MagmaChamber_GoblinTrader"] = function()
      return true
    end
  },
  ["MagmaChamber_East3_Lower"] = {
    ["MagmaChamber_East3_Upper"] = function()
      return swimming()
    end,
    ["HorizonBeach_Champion"] = function()
      return true
    end
  },
  ["MagmaChamber_Center1"] = {
    ["MagmaChamber_West3"] = function()
      return true
    end,
    ["MagmaChamber_Center2_Middle"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["MagmaChamber_Center2_Middle"] = {
    ["MagmaChamber_Center1"] = function()
      return true
    end,
    ["MagmaChamber_Center2_Lower"] = function()
      return magma_chamber_lower_lava()
    end,
    ["MagmaChamber_Center2_Upper"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end
  },
  ["MagmaChamber_Center2_Upper"] = {
    ["MagmaChamber_Center3"] = function()
      return true
    end,
    ["MagmaChamber_Center4_West"] = function()
      return true
    end,
    ["MagmaChamber_Center2_Middle"] = function()
      return true
    end
  },
  ["MagmaChamber_Center2_Lower"] = {
    ["MagmaChamber_Center5"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["MagmaChamber_Center2_Middle"] = function()
      return magma_chamber_lower_lava()
    end
  },
  ["MagmaChamber_Center3"] = {
    ["MagmaChamber_Center2_Upper"] = function()
      return true
    end
  },
  ["MagmaChamber_Center4_West"] = {
    ["MagmaChamber_Center2_Upper"] = function()
      return true
    end,
    ["MagmaChamber_Center4_East"] = function()
      return magma_chamber_center_shortcut()
    end
  },
  ["MagmaChamber_Center4_East"] = {
    ["MagmaChamber_Center4_West"] = function()
      return magma_chamber_center_shortcut()
    end,
    ["MagmaChamber_Center7"] = function()
      return true
    end
  },
  ["MagmaChamber_Center5"] = {
    ["MagmaChamber_Center2_Lower"] = function()
      return true
    end,
    ["MagmaChamber_CenterMagmaRoom"] = function()
      return true
    end,
    ["MagmaChamber_South1"] = function()
      return true
    end
  },
  ["MagmaChamber_Center6_Lower"] = {
    ["MagmaChamber_South2"] = function()
      return true
    end,
    ["MagmaChamber_Center6_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end
  },
  ["MagmaChamber_Center6_Upper"] = {
    ["MagmaChamber_Center7"] = function()
      return true
    end,
    ["MagmaChamber_Center6_Lower"] = function()
      return true
    end,
    ["MagmaChamber_AlchemistLab_West"] = function()
      return true
    end
  },
  ["MagmaChamber_Center7"] = {
    ["MagmaChamber_Center4_East"] = function()
      return true
    end,
    ["MagmaChamber_Center6_Upper"] = function()
      return true
    end,
    ["MagmaChamber_North8_West"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end
  },
  ["MagmaChamber_Center8"] = {
    ["MagmaChamber_Center9_Lower"] = function()
      return true
    end,
    ["MagmaChamber_AlchemistLab_East"] = function()
      return true
    end
  },
  ["MagmaChamber_Center9_Lower"] = {
    ["MagmaChamber_Center8"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["MagmaChamber_Center10"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["MagmaChamber_Center9_Middle"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["MagmaChamber_Center9_Middle"] = {
    ["MagmaChamber_Center9_Lower"] = function()
      return true
    end,
    ["MagmaChamber_Center9_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["MagmaChamber_PuppyRoom"] = function()
      return
      _OR({
        two_magma_chamber_keys(),
        minimal_locked_doors(),
        no_locked_doors()
      })
    end
  },
  ["MagmaChamber_Center9_Upper"] = {
    ["MagmaChamber_East1"] = function()
      return magma_chamber_east_shortcut()
    end,
    ["MagmaChamber_Center9_Middle"] = function()
      return true
    end
  },
  ["MagmaChamber_Center10"] = {
    ["MagmaChamber_South4_Upper"] = function()
      return true
    end,
    ["MagmaChamber_Center11"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility()
        })
      })
    end,
    ["MagmaChamber_Center9_Lower"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end
  },
  ["MagmaChamber_Center11"] = {
    ["MagmaChamber_Center10"] = function()
      return true
    end
  },
  ["MagmaChamber_South1"] = {
    ["MagmaChamber_Center5"] = function()
      return true
    end,
    ["MagmaChamber_South2"] = function()
      return true
    end
  },
  ["MagmaChamber_South2"] = {
    ["MagmaChamber_South1"] = function()
      return true
    end,
    ["MagmaChamber_Center6_Lower"] = function()
      return true
    end,
    ["MagmaChamber_South3_West"] = function()
      return true
    end
  },
  ["MagmaChamber_South3_West"] = {
    ["MagmaChamber_South2"] = function()
      return true
    end,
    ["MagmaChamber_South3_East"] = function()
      return magma_chamber_south_shortcut()
    end
  },
  ["MagmaChamber_South3_East"] = {
    ["MagmaChamber_South5"] = function()
      return true
    end,
    ["MagmaChamber_South3_West"] = function()
      return magma_chamber_south_shortcut()
    end
  },
  ["MagmaChamber_South4_Upper"] = {
    ["MagmaChamber_South4_Lower"] = function()
      return true
    end,
    ["MagmaChamber_Center10"] = function()
      return true
    end,
    ["MagmaChamber_Champion2"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end
  },
  ["MagmaChamber_South4_Lower"] = {
    ["MagmaChamber_South4_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["MagmaChamber_South6_East"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        mount()
      })
    end,
    ["MagmaChamber_South7_West"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["MagmaChamber_South5"] = {
    ["MagmaChamber_South6_West"] = function()
      return true
    end,
    ["MagmaChamber_South3_East"] = function()
      return true
    end,
    ["MagmaChamber_Champion"] = function()
      return true
    end,
    ["MagmaChamber_TarPit"] = function()
      return magic_walls()
    end
  },
  ["MagmaChamber_South6_East"] = {
    ["MagmaChamber_South6_West"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["MagmaChamber_South4_Lower"] = function()
      return true
    end
  },
  ["MagmaChamber_South6_West"] = {
    ["MagmaChamber_South6_East"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["MagmaChamber_South5"] = function()
      return true
    end
  },
  ["MagmaChamber_South7_East"] = {
    ["MagmaChamber_South7_West"] = function()
      return mount()
    end,
    ["MagmaChamber_South8"] = function()
      return breakable_walls()
    end
  },
  ["MagmaChamber_South7_West"] = {
    ["MagmaChamber_South7_East"] = function()
      return mount()
    end,
    ["MagmaChamber_South4_Lower"] = function()
      return true
    end
  },
  ["MagmaChamber_South8"] = {
    ["MagmaChamber_South7_East"] = function()
      return breakable_walls()
    end,
    ["MagmaChamber_South9_West"] = function()
      return true
    end
  },
  ["MagmaChamber_South9_West"] = {
    ["MagmaChamber_South8"] = function()
      return true
    end,
    ["MagmaChamber_South9_East"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["MagmaChamber_South9_East"] = {
    ["MagmaChamber_South9_Shortcut"] = function()
      return forgotten_world_to_magma_chamber_shortcut()
    end,
    ["MagmaChamber_South9_West"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["MagmaChamber_South9_Shortcut"] = {
    ["MagmaChamber_South9_East"] = function()
      return forgotten_world_to_magma_chamber_shortcut()
    end,
    ["ForgottenWorld_MCPath3"] = function()
      return forgotten_world_to_magma_chamber_shortcut()
    end
  },
  ["MagmaChamber_AlchemistLab_West"] = {
    ["MagmaChamber_Center6_Upper"] = function()
      return true
    end,
    ["MagmaChamber_AlchemistLab_East"] = function()
      return
      _OR({
        one_magma_chamber_key(),
        no_locked_doors()
      })
    end
  },
  ["MagmaChamber_AlchemistLab_East"] = {
    ["MagmaChamber_Center8"] = function()
      return true
    end,
    ["MagmaChamber_AlchemistLab_West"] = function()
      return
      _OR({
        one_magma_chamber_key(),
        no_locked_doors()
      })
    end
  },
  ["MagmaChamber_PuppyRoom"] = {
    ["MagmaChamber_Center9_Middle"] = function()
      return true
    end
  },
  ["MagmaChamber_CenterMagmaRoom"] = {
    ["MagmaChamber_Center5"] = function()
      return true
    end
  },
  ["MagmaChamber_TarPit"] = {
    ["MagmaChamber_South5"] = function()
      return true
    end
  },
  ["MagmaChamber_GoblinTrader"] = {
    ["MagmaChamber_East3"] = function()
      return true
    end
  },
  ["MagmaChamber_Champion"] = {
    ["MagmaChamber_South5"] = function()
      return true
    end
  },
  ["MagmaChamber_Champion2"] = {
    ["MagmaChamber_South4_Upper"] = function()
      return true
    end,
    ["MagmaChamber_LegendaryKeeperRoom"] = function()
      return levitate()
    end
  },
  ["MagmaChamber_LegendaryKeeperRoom"] = {
    ["MagmaChamber_Champion2"] = function()
      return true
    end
  },
  ["Underworld_Entrance"] = {
    ["BlueCave_South5"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["Underworld_East1"] = function()
      return true
    end
  },
  ["Underworld_East1"] = {
    ["Underworld_Entrance"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["Underworld_East2"] = function()
      return true
    end
  },
  ["Underworld_East2"] = {
    ["Underworld_East1"] = function()
      return true
    end,
    ["Underworld_East3"] = function()
      return true
    end
  },
  ["Underworld_East3"] = {
    ["Underworld_East2"] = function()
      return true
    end,
    ["Underworld_East4"] = function()
      return true
    end
  },
  ["Underworld_East4"] = {
    ["Underworld_East3"] = function()
      return true
    end,
    ["Underworld_East5"] = function()
      return true
    end
  },
  ["Underworld_East5"] = {
    ["Underworld_East4"] = function()
      return true
    end,
    ["Underworld_EastCatacomb1"] = function()
      return true
    end
  },
  ["Underworld_EastCatacomb1"] = {
    ["Underworld_East5"] = function()
      return true
    end,
    ["Underworld_EastCatacomb2"] = function()
      return true
    end,
    ["Underworld_EastCatacomb3"] = function()
      return true
    end,
    ["Underworld_EastCatacomb5"] = function()
      return true
    end
  },
  ["Underworld_EastCatacomb2"] = {
    ["Underworld_EastCatacomb1"] = function()
      return underworld_east_catacomb_7_access()
    end,
    ["Underworld_EastCatacomb7"] = function()
      return underworld_east_catacomb_7_access()
    end
  },
  ["Underworld_EastCatacomb3"] = {
    ["Underworld_EastCatacomb1"] = function()
      return true
    end,
    ["Underworld_EastCatacomb4"] = function()
      return
      _OR({
        underworld_key(),
        no_locked_doors()
      })
    end,
    ["Underworld_EastCatacomb8"] = function()
      return underworld_east_catacomb_8_shortcut()
    end,
    ["Underworld_Center1"] = function()
      return underworld_east_catacomb_pillar_control()
    end
  },
  ["Underworld_EastCatacomb4"] = {
    ["Underworld_EastCatacomb3"] = function()
      return
      _OR({
        underworld_key(),
        no_locked_doors()
      })
    end
  },
  ["Underworld_EastCatacomb5"] = {
    ["Underworld_EastCatacomb1"] = function()
      return true
    end,
    ["Underworld_EastCatacomb10"] = function()
      return true
    end,
    ["Underworld_EastCatacomb6_East"] = function()
      return true
    end,
    ["Underworld_EastCatacomb6_West"] = function()
      return underworld_east_catacomb_pillar_control()
    end
  },
  ["Underworld_EastCatacomb6_East"] = {
    ["Underworld_EastCatacomb5"] = function()
      return true
    end,
    ["Underworld_EastCatacomb6_West"] = function()
      return underworld_east_catacomb_6_shortcut()
    end
  },
  ["Underworld_EastCatacomb6_West"] = {
    ["Underworld_EastCatacomb6_East"] = function()
      return underworld_east_catacomb_6_shortcut()
    end
  },
  ["Underworld_EastCatacomb7"] = {
    ["Underworld_EastCatacomb2"] = function()
      return true
    end,
    ["Underworld_EastCatacomb8"] = function()
      return true
    end
  },
  ["Underworld_EastCatacomb8"] = {
    ["Underworld_EastCatacomb7"] = function()
      return true
    end,
    ["Underworld_EastCatacomb3"] = function()
      return true
    end,
    ["Underworld_EastCatacomb9"] = function()
      return
      _AND({
        heavy_blocks(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility()
        })
      })
    end
  },
  ["Underworld_EastCatacomb9"] = {
    ["Underworld_EastCatacomb8"] = function()
      return true
    end
  },
  ["Underworld_EastCatacomb10"] = {
    ["Underworld_EastCatacomb5"] = function()
      return true
    end
  },
  ["Underworld_Center1"] = {
    ["Underworld_Center2"] = function()
      return true
    end,
    ["Underworld_EastCatacomb2"] = function()
      return true
    end
  },
  ["Underworld_Center2"] = {
    ["Underworld_Center1"] = function()
      return true
    end,
    ["Underworld_Center3"] = function()
      return true
    end,
    ["Underworld_WestCatacomb2"] = function()
      return true
    end,
    ["Underworld_WestCatacomb6"] = function()
      return
      _AND({
        double_jump(),
        grapple(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end
  },
  ["Underworld_Center3"] = {
    ["Underworld_Center2"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        summon_big_rock()
      })
    end,
    ["Underworld_Center4"] = function()
      return true
    end,
    ["Underworld_CenterHidden"] = function()
      return
      _AND({
        double_jump(),
        narrow_corridors()
      })
    end
  },
  ["Underworld_CenterHidden"] = {
    ["Underworld_Center3"] = function()
      return
      _AND({
        double_jump(),
        narrow_corridors()
      })
    end
  },
  ["Underworld_Center4"] = {
    ["Underworld_Center3"] = function()
      return true
    end,
    ["Underworld_WestCatacomb4_Lower"] = function()
      return underworld_west_catacomb_center_entrance()
    end
  },
  ["Underworld_WestCatacomb1"] = {
    ["Underworld_WestCatacomb2"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end,
    ["Underworld_WestCatacomb3"] = function()
      return true
    end,
    ["Underworld_WestCatacomb4_Upper"] = function()
      return true
    end,
    ["Underworld_WestCatacomb4_West"] = function()
      return underworld_west_catacomb_4_access()
    end,
    ["Underworld_WestCatacomb5_East"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end,
    ["Underworld_WestCatacomb5_West"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["Underworld_WestCatacomb7_Shortcut"] = function()
      return true
    end,
    ["Underworld_WestCatacomb10"] = function()
      return
      _AND({
        double_jump(),
        grapple(),
        underworld_west_catacomb_roof_access()
      })
    end
  },
  ["Underworld_WestCatacomb2"] = {
    ["Underworld_Center2"] = function()
      return true
    end,
    ["Underworld_WestCatacomb1"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end
  },
  ["Underworld_WestCatacomb3"] = {
    ["Underworld_WestCatacomb1"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["Underworld_WestCatacomb4_West"] = function()
      return true
    end,
    ["Underworld_West1"] = function()
      return
      _AND({
        summon_big_rock(),
        double_jump(),
        grapple()
      })
    end
  },
  ["Underworld_WestCatacomb4_West"] = {
    ["Underworld_WestCatacomb3"] = function()
      return true
    end,
    ["Underworld_WestCatacomb1"] = function()
      return
      _AND({
        underworld_west_catacomb_4_access(),
        _OR({
          double_jump(),
          ground_switches(),
          distant_ledges()
        })
      })
    end
  },
  ["Underworld_WestCatacomb4_Lower"] = {
    ["Underworld_WestCatacomb4_Upper"] = function()
      return underworld_west_catacomb_4_shortcut()
    end,
    ["Underworld_Center4"] = function()
      return underworld_west_catacomb_center_entrance()
    end
  },
  ["Underworld_WestCatacomb4_Upper"] = {
    ["Underworld_WestCatacomb4_Lower"] = function()
      return underworld_west_catacomb_4_shortcut()
    end,
    ["Underworld_WestCatacomb1"] = function()
      return true
    end
  },
  ["Underworld_WestCatacomb5_East"] = {
    ["Underworld_WestCatacomb1"] = function()
      return true
    end,
    ["Underworld_WestCatacomb6"] = function()
      return true
    end,
    ["Underworld_WestCatacomb9_Interior"] = function()
      return underworld_west_catacomb_9_interior_access()
    end
  },
  ["Underworld_WestCatacomb5_West"] = {
    ["Underworld_WestCatacomb1"] = function()
      return true
    end,
    ["Underworld_WestCatacomb7"] = function()
      return true
    end
  },
  ["Underworld_WestCatacomb6"] = {
    ["Underworld_WestCatacomb5_East"] = function()
      return true
    end,
    ["Underworld_Center2"] = function()
      return true
    end,
    ["Underworld_WestCatacomb9_ExteriorEast"] = function()
      return
      _AND({
        double_jump(),
        grapple()
      })
    end
  },
  ["Underworld_WestCatacomb7"] = {
    ["Underworld_WestCatacomb7_Shortcut"] = function()
      return underworld_west_catacomb_7_shortcut()
    end,
    ["Underworld_WestCatacomb8"] = function()
      return true
    end
  },
  ["Underworld_WestCatacomb7_Shortcut"] = {
    ["Underworld_WestCatacomb7"] = function()
      return underworld_west_catacomb_7_shortcut()
    end,
    ["Underworld_WestCatacomb1"] = function()
      return true
    end
  },
  ["Underworld_WestCatacomb8"] = {
    ["Underworld_WestCatacomb7"] = function()
      return true
    end,
    ["Underworld_WestCatacomb9_ExteriorWest"] = function()
      return true
    end
  },
  ["Underworld_WestCatacomb9_ExteriorWest"] = {
    ["Underworld_WestCatacomb8"] = function()
      return true
    end
  },
  ["Underworld_WestCatacomb9_ExteriorEast"] = {
    ["Underworld_WestCatacomb6"] = function()
      return true
    end,
    ["Underworld_WestCatacomb9_Roof"] = function()
      return underworld_west_catacomb_roof_access()
    end
  },
  ["Underworld_WestCatacomb9_Roof"] = {
    ["Underworld_WestCatacomb9_ExteriorEast"] = function()
      return true
    end,
    ["Underworld_WestCatacomb9_ExteriorWest"] = function()
      return true
    end
  },
  ["Underworld_WestCatacomb9_Interior"] = {
    ["Underworld_WestCatacomb5_East"] = function()
      return underworld_west_catacomb_9_interior_access()
    end
  },
  ["Underworld_WestCatacomb10"] = {
    ["Underworld_WestCatacomb1"] = function()
      return true
    end
  },
  ["Underworld_West1"] = {
    ["Underworld_WestCatacomb3"] = function()
      return true
    end,
    ["Underworld_West2"] = function()
      return true
    end,
    ["SunPalace_EastSewers6"] = function()
      return underworld_to_sun_palace_shortcut()
    end
  },
  ["Underworld_West2"] = {
    ["Underworld_West1"] = function()
      return true
    end,
    ["Underworld_West3"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["Underworld_West3"] = {
    ["Underworld_West2"] = function()
      return true
    end,
    ["Underworld_West4"] = function()
      return true
    end,
    ["Underworld_West5"] = function()
      return true
    end
  },
  ["Underworld_West4"] = {
    ["Underworld_West3"] = function()
      return true
    end,
    ["Underworld_West6"] = function()
      return true
    end
  },
  ["Underworld_West5"] = {
    ["Underworld_West3"] = function()
      return true
    end,
    ["Underworld_West6"] = function()
      return true
    end
  },
  ["Underworld_West6"] = {
    ["Underworld_West4"] = function()
      return true
    end,
    ["Underworld_West5"] = function()
      return true
    end
  },
  ["MysticalWorkshop_South1"] = {
    ["MysticalWorkshop_South2"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["MysticalWorkshop_South6"] = function()
      return breakable_walls()
    end,
    ["StrongholdDungeon_North4"] = function()
      return true
    end
  },
  ["MysticalWorkshop_South2"] = {
    ["MysticalWorkshop_South1"] = function()
      return true
    end,
    ["MysticalWorkshop_South3_Middle"] = function()
      return true
    end
  },
  ["MysticalWorkshop_South3_Middle"] = {
    ["MysticalWorkshop_South2"] = function()
      return true
    end,
    ["MysticalWorkshop_South4"] = function()
      return true
    end,
    ["MysticalWorkshop_South3_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        summon_big_rock()
      })
    end,
    ["MysticalWorkshop_South3_Lower"] = function()
      return true
    end
  },
  ["MysticalWorkshop_South3_Lower"] = {
    ["MysticalWorkshop_South5"] = function()
      return true
    end,
    ["MysticalWorkshop_South3_Middle"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end
  },
  ["MysticalWorkshop_South3_Upper"] = {
    ["MysticalWorkshop_Center2"] = function()
      return true
    end,
    ["MysticalWorkshop_South3_Middle"] = function()
      return true
    end
  },
  ["MysticalWorkshop_South4"] = {
    ["MysticalWorkshop_South3_Lower"] = function()
      return true
    end
  },
  ["MysticalWorkshop_South5"] = {
    ["MysticalWorkshop_South3_Lower"] = function()
      return true
    end
  },
  ["MysticalWorkshop_South6"] = {
    ["MysticalWorkshop_South1"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Center1_Lower"] = {
    ["MysticalWorkshop_Center1_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        summon_big_rock()
      })
    end,
    ["MysticalWorkshop_Center2"] = function()
      return true
    end,
    ["MysticalWorkshop_Center6"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Center1_Upper"] = {
    ["MysticalWorkshop_Center1_Lower"] = function()
      return true
    end,
    ["MysticalWorkshop_Center4"] = function()
      return true
    end,
    ["MysticalWorkshop_West3_Access"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Center2"] = {
    ["MysticalWorkshop_Center1_Lower"] = function()
      return true
    end,
    ["MysticalWorkshop_South3_Upper"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Center3"] = {
    ["MysticalWorkshop_Center8"] = function()
      return true
    end,
    ["MysticalWorkshop_East1"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["MysticalWorkshop_Center4"] = {
    ["MysticalWorkshop_Center1_Upper"] = function()
      return true
    end,
    ["MysticalWorkshop_Center5_Lower"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end
  },
  ["MysticalWorkshop_Center5_Lower"] = {
    ["MysticalWorkshop_Center4"] = function()
      return true
    end,
    ["MysticalWorkshop_Center5_Middle"] = function()
      return
      _AND({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["MysticalWorkshop_Center5_Middle"] = {
    ["MysticalWorkshop_Center8"] = function()
      return true
    end,
    ["MysticalWorkshop_Center9"] = function()
      return true
    end,
    ["MysticalWorkshop_Center5_Lower"] = function()
      return true
    end,
    ["MysticalWorkshop_Center5_Upper"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end
  },
  ["MysticalWorkshop_Center5_Upper"] = {
    ["MysticalWorkshop_Center5_Middle"] = function()
      return true
    end,
    ["MysticalWorkshop_Center7"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Center6"] = {
    ["MysticalWorkshop_Center2_Lower"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges(),
        mount()
      })
    end,
    ["MysticalWorkshop_GolemMerchant"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Center7"] = {
    ["MysticalWorkshop_Center5_Upper"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Center8"] = {
    ["MysticalWorkshop_Center5_Middle"] = function()
      return true
    end,
    ["MysticalWorkshop_West1"] = function()
      return true
    end,
    ["MysticalWorkshop_Center3"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Center9"] = {
    ["MysticalWorkshop_Center5_Middle"] = function()
      return true
    end
  },
  ["MysticalWorkshop_West1"] = {
    ["MysticalWorkshop_West2"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end,
    ["MysticalWorkshop_Center8"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end
  },
  ["MysticalWorkshop_West2"] = {
    ["MysticalWorkshop_West1"] = function()
      return true
    end
  },
  ["MysticalWorkshop_West3_Access"] = {
    ["MysticalWorkshop_Center1_Lower"] = function()
      return true
    end,
    ["MysticalWorkshop_West3"] = function()
      return abandoned_tower_access()
    end
  },
  ["MysticalWorkshop_West3"] = {
    ["AbandonedTower_Entrance"] = function()
      return true
    end,
    ["MysticalWorkshop_West3_Access"] = function()
      return abandoned_tower_access()
    end
  },
  ["MysticalWorkshop_East1"] = {
    ["MysticalWorkshop_Center3"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end,
    ["MysticalWorkshop_East2"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end,
    ["MysticalWorkshop_North1"] = function()
      return
      _OR({
        double_jump(),
        ground_switches(),
        distant_ledges()
      })
    end
  },
  ["MysticalWorkshop_East2"] = {
    ["MysticalWorkshop_East1"] = function()
      return true
    end,
    ["MysticalWorkshop_East3"] = function()
      return true
    end,
    ["MysticalWorkshop_North2"] = function()
      return true
    end
  },
  ["MysticalWorkshop_East3"] = {
    ["MysticalWorkshop_East2"] = function()
      return true
    end
  },
  ["MysticalWorkshop_North1"] = {
    ["MysticalWorkshop_East1"] = function()
      return true
    end,
    ["MysticalWorkshop_North3"] = function()
      return true
    end,
    ["MysticalWorkshop_North6"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        summon_big_rock()
      })
    end
  },
  ["MysticalWorkshop_North2"] = {
    ["MysticalWorkshop_East2"] = function()
      return true
    end,
    ["MysticalWorkshop_North4_Shortcut"] = function()
      return true
    end
  },
  ["MysticalWorkshop_North3"] = {
    ["MysticalWorkshop_North1"] = function()
      return true
    end
  },
  ["MysticalWorkshop_North4_Lower"] = {
    ["MysticalWorkshop_North4_Shortcut"] = function()
      return mystical_workshop_north_shortcut()
    end,
    ["MysticalWorkshop_North6"] = function()
      return true
    end,
    ["MysticalWorkshop_North4_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["MysticalWorkshop_North4_Upper"] = {
    ["MysticalWorkshop_North4_Lower"] = function()
      return true
    end,
    ["MysticalWorkshop_Clock"] = function()
      return true
    end,
    ["MysticalWorkshop_North5"] = function()
      return true
    end
  },
  ["MysticalWorkshop_North4_Shortcut"] = {
    ["MysticalWorkshop_North4_Lower"] = function()
      return mystical_workshop_north_shortcut()
    end,
    ["MysticalWorkshop_North2"] = function()
      return true
    end
  },
  ["MysticalWorkshop_North5"] = {
    ["MysticalWorkshop_North4_Upper"] = function()
      return true
    end,
    ["MysticalWorkshop_MadEyeRoom"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end
  },
  ["MysticalWorkshop_North6"] = {
    ["MysticalWorkshop_North1"] = function()
      return true
    end,
    ["MysticalWorkshop_North4_Lower"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          three_workshop_keys(),
          no_locked_doors()
        })
      })
    end
  },
  ["MysticalWorkshop_Clock"] = {
    ["MysticalWorkshop_North4_Upper"] = function()
      return true
    end,
    ["MysticalWorkshop_Hidden"] = function()
      return true
    end,
    ["MysticalWorkshop_Vertraag"] = function()
      return true
    end
  },
  ["MysticalWorkshop_GolemMerchant"] = {
    ["MysticalWorkshop_Center6"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Hidden"] = {
    ["MysticalWorkshop_Clock"] = function()
      return true
    end
  },
  ["MysticalWorkshop_Vertraag"] = {
    ["MysticalWorkshop_Clock"] = function()
      return true
    end
  },
  ["MysticalWorkshop_MadEyeRoom"] = {
    ["MysticalWorkshop_North5"] = function()
      return true
    end
  },
  ["BlobBurg_East1"] = {
    ["MagmaChamber_West7"] = function()
      return true
    end,
    ["BlobBurg_East2"] = function()
      return true
    end
  },
  ["BlobBurg_East2"] = {
    ["BlobBurg_East1"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["BlobBurg_East3"] = function()
      return true
    end,
    ["BlobBurg_EastHidden"] = function()
      return
      _AND({
        narrow_corridors(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end
  },
  ["BlobBurg_East3"] = {
    ["BlobBurg_East2"] = function()
      return true
    end,
    ["BlobBurg_Center1"] = function()
      return true
    end
  },
  ["BlobBurg_East4"] = {
    ["BlobBurg_Center1"] = function()
      return true
    end,
    ["BlobBurg_East5"] = function()
      return true
    end
  },
  ["BlobBurg_East5"] = {
    ["BlobBurg_East4"] = function()
      return true
    end
  },
  ["BlobBurg_EastHidden"] = {
    ["BlobBurg_East2"] = function()
      return true
    end
  },
  ["BlobBurg_Center1"] = {
    ["BlobBurg_East3"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["BlobBurg_Center3"] = function()
      return
      _AND({
        blob_burg_access_2(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility()
        })
      })
    end,
    ["BlobBurg_Center2"] = function()
      return true
    end,
    ["BlobBurg_East4"] = function()
      return blob_burg_access_1()
    end
  },
  ["BlobBurg_Center2"] = {
    ["BlobBurg_Center1"] = function()
      return true
    end,
    ["BlobBurg_Center4"] = function()
      return blob_burg_access_3()
    end
  },
  ["BlobBurg_Center3"] = {
    ["BlobBurg_Center1"] = function()
      return true
    end,
    ["BlobBurg_Worms"] = function()
      return blob_burg_access_6()
    end
  },
  ["BlobBurg_Center4"] = {
    ["BlobBurg_Center2"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end,
    ["BlobBurg_South1"] = function()
      return true
    end,
    ["BlobBurg_West1"] = function()
      return blob_burg_access_4()
    end,
    ["BlobBurg_Center5"] = function()
      return
      _AND({
        blob_burg_access_5(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility()
        })
      })
    end
  },
  ["BlobBurg_Center5"] = {
    ["BlobBurg_Center4"] = function()
      return true
    end,
    ["BlobBurg_Champion"] = function()
      return true
    end
  },
  ["BlobBurg_West1"] = {
    ["BlobBurg_Center4"] = function()
      return swimming()
    end,
    ["BlobBurg_West2"] = function()
      return swimming()
    end
  },
  ["BlobBurg_West2"] = {
    ["BlobBurg_West1"] = function()
      return true
    end
  },
  ["BlobBurg_South1"] = {
    ["BlobBurg_Center4"] = function()
      return
      _OR({
        swimming(),
        double_jump()
      })
    end,
    ["BlobBurg_South2"] = function()
      return
      _OR({
        swimming(),
        double_jump()
      })
    end
  },
  ["BlobBurg_South2"] = {
    ["BlobBurg_South1"] = function()
      return true
    end
  },
  ["BlobBurg_Champion"] = {
    ["BlobBurg_Center5"] = function()
      return true
    end
  },
  ["BlobBurg_Worms"] = {
    ["BlobBurg_Center3"] = function()
      return true
    end
  },
  ["ForgottenWorld_Fall1"] = {
    ["ForgottenWorld_Fall2"] = function()
      return true
    end,
    ["ForgottenWorld_FallHidden"] = function()
      return dark_rooms()
    end
  },
  ["ForgottenWorld_FallHidden"] = {
    ["ForgottenWorld_Fall1"] = function()
      return true
    end
  },
  ["ForgottenWorld_Fall2"] = {
    ["ForgottenWorld_ForgottenWorldIntro"] = function()
      return true
    end
  },
  ["ForgottenWorld_ForgottenWorldIntro"] = {
    ["ForgottenWorld_Fall2"] = function()
      return true
    end,
    ["ForgottenWorld_Jungle1"] = function()
      return
      _OR({
        swimming(),
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end
  },
  ["ForgottenWorld_Jungle1"] = {
    ["ForgottenWorld_Jungle2"] = function()
      return true
    end,
    ["ForgottenWorld_Caves1"] = function()
      return true
    end,
    ["ForgottenWorld_ForgottenWorldIntro"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["ForgottenWorld_Jungle2"] = {
    ["ForgottenWorld_Jungle1"] = function()
      return true
    end,
    ["ForgottenWorld_Jungle3"] = function()
      return true
    end
  },
  ["ForgottenWorld_Jungle3"] = {
    ["ForgottenWorld_Jungle2"] = function()
      return true
    end,
    ["ForgottenWorld_Jungle4"] = function()
      return true
    end,
    ["ForgottenWorld_JungleHidden"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          improved_flying(),
          dual_mobility(),
          lofty_mount(),
          summon_big_rock()
        })
      })
    end
  },
  ["ForgottenWorld_Jungle4"] = {
    ["ForgottenWorld_Jungle3"] = function()
      return true
    end,
    ["ForgottenWorld_Jungle5"] = function()
      return true
    end,
    ["ForgottenWorld_JungleShortcut"] = function()
      return forgotten_world_jungle_shortcut()
    end
  },
  ["ForgottenWorld_Jungle5"] = {
    ["ForgottenWorld_Jungle4"] = function()
      return true
    end,
    ["ForgottenWorld_Jungle6"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end,
    ["ForgottenWorld_TarPits1"] = function()
      return magic_vines()
    end
  },
  ["ForgottenWorld_Jungle5_Hidden"] = {
    ["ForgottenWorld_TarPitsHidden1"] = function()
      return true
    end
  },
  ["ForgottenWorld_Jungle6"] = {
    ["ForgottenWorld_Jungle5"] = function()
      return true
    end,
    ["ForgottenWorld_Climb1"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end
  },
  ["ForgottenWorld_JungleHidden"] = {
    ["ForgottenWorld_Jungle3"] = function()
      return true
    end
  },
  ["ForgottenWorld_JungleShortcut"] = {
    ["ForgottenWorld_TarPits8"] = function()
      return true
    end,
    ["ForgottenWorld_Jungle4"] = function()
      return forgotten_world_jungle_shortcut()
    end
  },
  ["ForgottenWorld_TarPits1"] = {
    ["ForgottenWorld_Jungle5"] = function()
      return true
    end,
    ["ForgottenWorld_TarPits2"] = function()
      return true
    end,
    ["ForgottenWorld_TarPitsHidden1"] = function()
      return
      _AND({
        tar(),
        double_jump(),
        breakable_walls()
      })
    end
  },
  ["ForgottenWorld_TarPits2"] = {
    ["ForgottenWorld_TarPits1"] = function()
      return true
    end,
    ["ForgottenWorld_TarPits3"] = function()
      return true
    end
  },
  ["ForgottenWorld_TarPits3"] = {
    ["ForgottenWorld_TarPits2"] = function()
      return
      _AND({
        tar(),
        double_jump()
      })
    end,
    ["ForgottenWorld_TarPits4"] = function()
      return true
    end
  },
  ["ForgottenWorld_TarPits4"] = {
    ["ForgottenWorld_TarPits3"] = function()
      return true
    end,
    ["ForgottenWorld_TarPits5_Upper"] = function()
      return true
    end
  },
  ["ForgottenWorld_TarPits5_Upper"] = {
    ["ForgottenWorld_TarPits4"] = function()
      return true
    end,
    ["ForgottenWorld_TarPits5_Lower"] = function()
      return true
    end,
    ["ForgottenWorld_TarPits6"] = function()
      return true
    end
  },
  ["ForgottenWorld_TarPits5_Lower"] = {
    ["ForgottenWorld_Waters5"] = function()
      return true
    end,
    ["ForgottenWorld_TarPits5_Upper"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        ground_switches()
      })
    end,
    ["ForgottenWorld_TarPits9"] = function()
      return true
    end
  },
  ["ForgottenWorld_TarPits6"] = {
    ["ForgottenWorld_TarPits5_Upper"] = function()
      return true
    end,
    ["ForgottenWorld_TarPits7"] = function()
      return true
    end
  },
  ["ForgottenWorld_TarPits7"] = {
    ["ForgottenWorld_TarPits6"] = function()
      return true
    end,
    ["ForgottenWorld_TarPits8"] = function()
      return true
    end,
    ["ForgottenWorld_WorldTree"] = function()
      return true
    end
  },
  ["ForgottenWorld_TarPits8"] = {
    ["ForgottenWorld_TarPits7"] = function()
      return true
    end,
    ["ForgottenWorld_JungleShortcut"] = function()
      return
      _OR({
        double_jump(),
        summon_big_rock(),
        distant_ledges()
      })
    end
  },
  ["ForgottenWorld_TarPits9"] = {
    ["ForgottenWorld_TarPits5_Lower"] = function()
      return true
    end
  },
  ["ForgottenWorld_TarPitsHidden1"] = {
    ["ForgottenWorld_Jungle5_Hidden"] = function()
      return true
    end,
    ["ForgottenWorld_TarPits1"] = function()
      return true
    end
  },
  ["ForgottenWorld_Waters1_Upper"] = {
    ["ForgottenWorld_WorldTree"] = function()
      return magic_walls()
    end,
    ["ForgottenWorld_Waters1_Middle"] = function()
      return true
    end
  },
  ["ForgottenWorld_Waters1_Middle"] = {
    ["ForgottenWorld_Waters5"] = function()
      return true
    end,
    ["ForgottenWorld_DracomerLair"] = function()
      return
      _AND({
        swimming(),
        forgotten_world_waters_shortcut()
      })
    end,
    ["ForgottenWorld_Waters1_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["ForgottenWorld_Waters1_Lower"] = function()
      return true
    end
  },
  ["ForgottenWorld_Waters1_Lower"] = {
    ["ForgottenWorld_Waters2"] = function()
      return true
    end,
    ["ForgottenWorld_Waters1_Middle"] = function()
      return swimming()
    end
  },
  ["ForgottenWorld_Waters2"] = {
    ["ForgottenWorld_Waters3"] = function()
      return true
    end,
    ["ForgottenWorld_Waters1_Lower"] = function()
      return swimming()
    end
  },
  ["ForgottenWorld_Waters3"] = {
    ["ForgottenWorld_Waters2"] = function()
      return true
    end,
    ["ForgottenWorld_Waters4"] = function()
      return swimming()
    end
  },
  ["ForgottenWorld_Waters4"] = {
    ["ForgottenWorld_Waters3"] = function()
      return swimming()
    end,
    ["ForgottenWorld_DracomerLair"] = function()
      return improved_swimming()
    end,
    ["ForgottenWorld_WatersHidden"] = function()
      return improved_swimming()
    end
  },
  ["ForgottenWorld_Waters5"] = {
    ["ForgottenWorld_Waters1_Middle"] = function()
      return magic_walls()
    end,
    ["ForgottenWorld_TarPits5_Lower"] = function()
      return
      _AND({
        magic_walls(),
        _OR({
          summon_big_rock(),
          double_jump(),
          improved_flying(),
          dual_mobility(),
          lofty_mount()
        })
      })
    end
  },
  ["ForgottenWorld_WatersHidden"] = {
    ["ForgottenWorld_Waters4"] = function()
      return true
    end
  },
  ["ForgottenWorld_DracomerLair"] = {
    ["ForgottenWorld_Waters4"] = function()
      return true
    end,
    ["ForgottenWorld_Waters1_Middle"] = function()
      return forgotten_world_waters_shortcut()
    end
  },
  ["ForgottenWorld_Caves1"] = {
    ["ForgottenWorld_Caves2_Upper"] = function()
      return true
    end,
    ["ForgottenWorld_Caves4"] = function()
      return true
    end,
    ["ForgottenWorld_Jungle1"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves2_Upper"] = {
    ["ForgottenWorld_Caves1"] = function()
      return true
    end,
    ["ForgottenWorld_Caves3"] = function()
      return true
    end,
    ["ForgottenWorld_MCPath1"] = function()
      return true
    end,
    ["ForgottenWorld_Caves2_Lower"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves2_Lower"] = {
    ["ForgottenWorld_Caves2_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["ForgottenWorld_Caves5_Upper"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves3"] = {
    ["ForgottenWorld_Caves2_Upper"] = function()
      return true
    end,
    ["ForgottenWorld_Caves11"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves4"] = {
    ["ForgottenWorld_Caves1"] = function()
      return true
    end,
    ["ForgottenWorld_Caves5_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["ForgottenWorld_Caves6"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["ForgottenWorld_Caves5_Lower"] = {
    ["ForgottenWorld_Caves8"] = function()
      return true
    end,
    ["ForgottenWorld_Caves9"] = function()
      return true
    end,
    ["ForgottenWorld_Caves5_Upper"] = function()
      return
      _OR({
        double_jump(),
        magic_vines()
      })
    end
  },
  ["ForgottenWorld_Caves5_Upper"] = {
    ["ForgottenWorld_Caves2_Lower"] = function()
      return
      _AND({
        double_jump(),
        magic_vines()
      })
    end,
    ["ForgottenWorld_Caves4"] = function()
      return
      _AND({
        double_jump(),
        magic_vines()
      })
    end,
    ["ForgottenWorld_Caves5_Lower"] = function()
      return
      _AND({
        double_jump(),
        magic_vines()
      })
    end
  },
  ["ForgottenWorld_Caves6"] = {
    ["ForgottenWorld_Caves4"] = function()
      return true
    end,
    ["ForgottenWorld_Caves7"] = function()
      return true
    end,
    ["ForgottenWorld_Caves8"] = function()
      return true
    end,
    ["ForgottenWorld_Caves12"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves7"] = {
    ["ForgottenWorld_Caves6"] = function()
      return true
    end,
    ["ForgottenWorld_WorldTree"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves8"] = {
    ["ForgottenWorld_Caves5"] = function()
      return true
    end,
    ["ForgottenWorld_Caves6"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves9"] = {
    ["ForgottenWorld_Caves5_Lower"] = function()
      return true
    end,
    ["ForgottenWorld_Caves10"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves10"] = {
    ["ForgottenWorld_Caves9"] = function()
      return true
    end,
    ["ForgottenWorld_Caves11_Lower"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["ForgottenWorld_CavesStudy"] = function()
      return true
    end,
    ["ForgottenWorld_TerradrileLair1"] = function()
      return
      _AND({
        diamond_blocks(),
        breakable_walls()
      })
    end
  },
  ["ForgottenWorld_Caves11_Upper"] = {
    ["ForgottenWorld_Caves11_Lower"] = function()
      return forgotten_world_caves_shortcut()
    end,
    ["ForgottenWorld_Caves3"] = function()
      return true
    end,
    ["ForgottenWorld_WandererRoom"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves11_Lower"] = {
    ["ForgottenWorld_Caves11_Upper"] = function()
      return
      _AND({
        forgotten_world_caves_shortcut(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility()
        })
      })
    end,
    ["ForgottenWorld_Caves10"] = function()
      return true
    end
  },
  ["ForgottenWorld_Caves12"] = {
    ["ForgottenWorld_DarkRoom"] = function()
      return true
    end,
    ["ForgottenWorld_Caves6"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["ForgottenWorld_DarkRoom"] = {
    ["ForgottenWorld_Caves12"] = function()
      return true
    end
  },
  ["ForgottenWorld_CavesStudy"] = {
    ["ForgottenWorld_Caves10"] = function()
      return true
    end
  },
  ["ForgottenWorld_WandererRoom"] = {
    ["ForgottenWorld_Caves11_Upper"] = function()
      return true
    end
  },
  ["ForgottenWorld_WorldTree"] = {
    ["ForgottenWorld_TarPits7"] = function()
      return true
    end,
    ["ForgottenWorld_Caves7"] = function()
      return true
    end,
    ["ForgottenWorld_Waters1_Upper"] = function()
      return magic_walls()
    end
  },
  ["ForgottenWorld_TerradrileLair1"] = {
    ["ForgottenWorld_Caves10"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["ForgottenWorld_TerradrileLair2"] = function()
      return
      _AND({
        breakable_walls(),
        narrow_corridors()
      })
    end
  },
  ["ForgottenWorld_TerradrileLair2"] = {
    ["ForgottenWorld_TerradrileLair1"] = function()
      return true
    end
  },
  ["ForgottenWorld_MCPath1"] = {
    ["ForgottenWorld_MCPath2"] = function()
      return
      _AND({
        double_jump(),
        _OR({
          double_jump(),
          improved_flying(),
          dual_mobility()
        })
      })
    end,
    ["ForgottenWorld_Caves2_Upper"] = function()
      return true
    end
  },
  ["ForgottenWorld_MCPath2"] = {
    ["ForgottenWorld_MCPath1"] = function()
      return true
    end,
    ["ForgottenWorld_MCPath3"] = function()
      return true
    end
  },
  ["ForgottenWorld_MCPath3"] = {
    ["ForgottenWorld_MCPath2"] = function()
      return true
    end,
    ["MagmaChamber_South9_Shortcut"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["ForgottenWorld_Climb1"] = {
    ["ForgottenWorld_Jungle6"] = function()
      return true
    end,
    ["ForgottenWorld_Climb2"] = function()
      return true
    end,
    ["ForgottenWorld_ClimbPuzzle"] = function()
      return impassible_vines()
    end
  },
  ["ForgottenWorld_ClimbPuzzle"] = {
    ["ForgottenWorld_Climb1"] = function()
      return true
    end
  },
  ["ForgottenWorld_Climb2"] = {
    ["ForgottenWorld_Climb1"] = function()
      return true
    end,
    ["ForgottenWorld_Climb3"] = function()
      return true
    end
  },
  ["ForgottenWorld_Climb3"] = {
    ["ForgottenWorld_Climb2"] = function()
      return true
    end,
    ["ForgottenWorld_Climb4"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["ForgottenWorld_Climb4"] = {
    ["ForgottenWorld_Climb3"] = function()
      return true
    end,
    ["ForgottenWorld_ClimbSide"] = function()
      return true
    end,
    ["ForgottenWorld_Climb5"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["ForgottenWorld_Climb5"] = {
    ["ForgottenWorld_Climb4"] = function()
      return true
    end,
    ["HorizonBeach_FWExit"] = function()
      return true
    end
  },
  ["ForgottenWorld_ClimbSide"] = {
    ["ForgottenWorld_Climb4"] = function()
      return true
    end
  },
  ["AbandonedTower_Entrance"] = {
    ["MysticalWorkshop_West3"] = function()
      return true
    end,
    ["AbandonedTower_South1"] = function()
      return key_of_power()
    end
  },
  ["AbandonedTower_South1"] = {
    ["AbandonedTower_Entrance"] = function()
      return true
    end,
    ["AbandonedTower_South2"] = function()
      return true
    end,
    ["AbandonedTower_South3_Lower"] = function()
      return true
    end
  },
  ["AbandonedTower_South2"] = {
    ["AbandonedTower_South1"] = function()
      return true
    end,
    ["AbandonedTower_South4"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end
  },
  ["AbandonedTower_South3_Lower"] = {
    ["AbandonedTower_South1"] = function()
      return true
    end,
    ["AbandonedTower_South3_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end
  },
  ["AbandonedTower_South3_Upper"] = {
    ["AbandonedTower_South3_Lower"] = function()
      return true
    end,
    ["AbandonedTower_South4"] = function()
      return true
    end
  },
  ["AbandonedTower_South4"] = {
    ["AbandonedTower_South2"] = function()
      return true
    end,
    ["AbandonedTower_South3_Upper"] = function()
      return true
    end,
    ["AbandonedTower_South5"] = function()
      return true
    end
  },
  ["AbandonedTower_South5"] = {
    ["AbandonedTower_South4"] = function()
      return true
    end,
    ["AbandonedTower_South7"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end
  },
  ["AbandonedTower_South6"] = {
    ["AbandonedTower_South7"] = function()
      return true
    end,
    ["AbandonedTower_Center1_Lower"] = function()
      return double_jump()
    end
  },
  ["AbandonedTower_South7"] = {
    ["AbandonedTower_South5"] = function()
      return true
    end,
    ["AbandonedTower_South6"] = function()
      return true
    end,
    ["AbandonedTower_South8"] = function()
      return true
    end,
    ["AbandonedTower_SouthHidden1"] = function()
      return breakable_walls()
    end,
    ["AbandonedTower_SouthHidden2"] = function()
      return narrow_corridors()
    end
  },
  ["AbandonedTower_South8"] = {
    ["AbandonedTower_South7"] = function()
      return true
    end,
    ["AbandonedTower_South8_Shortcut"] = function()
      return abandoned_tower_south_shortcut()
    end
  },
  ["AbandonedTower_South8_Shortcut"] = {
    ["AbandonedTower_Center3_Lower"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount()
      })
    end,
    ["AbandonedTower_South8"] = function()
      return abandoned_tower_south_shortcut()
    end
  },
  ["AbandonedTower_SouthHidden1"] = {
    ["AbandonedTower_South7"] = function()
      return true
    end
  },
  ["AbandonedTower_SouthHidden2"] = {
    ["AbandonedTower_South7"] = function()
      return true
    end
  },
  ["AbandonedTower_Center1_Lower"] = {
    ["AbandonedTower_South6"] = function()
      return true
    end,
    ["AbandonedTower_Center1_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["AbandonedTower_Center1_Upper"] = {
    ["AbandonedTower_Center1_Lower"] = function()
      return true
    end,
    ["AbandonedTower_Center2"] = function()
      return true
    end,
    ["AbandonedTower_Center3_Upper"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["AbandonedTower_Center2"] = {
    ["AbandonedTower_Center1_Upper"] = function()
      return true
    end
  },
  ["AbandonedTower_Center3_Lower"] = {
    ["AbandonedTower_South8_Shortcut"] = function()
      return true
    end,
    ["AbandonedTower_Center3_Upper"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges()
      })
    end
  },
  ["AbandonedTower_Center3_Upper"] = {
    ["AbandonedTower_Center3_Lower"] = function()
      return true
    end,
    ["AbandonedTower_Center1_Upper"] = function()
      return true
    end,
    ["AbandonedTower_Center4"] = function()
      return true
    end
  },
  ["AbandonedTower_Center4"] = {
    ["AbandonedTower_Center3_Upper"] = function()
      return true
    end,
    ["AbandonedTower_Center5"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["AbandonedTower_Center5"] = {
    ["AbandonedTower_Center4"] = function()
      return true
    end,
    ["AbandonedTower_Center6"] = function()
      return true
    end
  },
  ["AbandonedTower_Center6"] = {
    ["AbandonedTower_Center5"] = function()
      return true
    end,
    ["AbandonedTower_Center7"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end
  },
  ["AbandonedTower_Center7"] = {
    ["AbandonedTower_Center6"] = function()
      return true
    end,
    ["AbandonedTower_Center8"] = function()
      return true
    end,
    ["AbandonedTower_Center10"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["AbandonedTower_Center8"] = {
    ["AbandonedTower_Center7"] = function()
      return true
    end,
    ["AbandonedTower_Center9"] = function()
      return true
    end
  },
  ["AbandonedTower_Center9"] = {
    ["AbandonedTower_Center8"] = function()
      return true
    end,
    ["AbandonedTower_Center11"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end,
    ["AbandonedTower_Center12"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["AbandonedTower_Center10"] = {
    ["AbandonedTower_Center7"] = function()
      return true
    end,
    ["AbandonedTower_Center10_Shortcut"] = function()
      return abandoned_tower_center_shortcut()
    end
  },
  ["AbandonedTower_Center10_Shortcut"] = {
    ["AbandonedTower_Center7"] = function()
      return true
    end,
    ["AbandonedTower_Center10"] = function()
      return abandoned_tower_center_shortcut()
    end,
    ["AbandonedTower_Center12"] = function()
      return true
    end
  },
  ["AbandonedTower_Center11"] = {
    ["AbandonedTower_Center9"] = function()
      return true
    end
  },
  ["AbandonedTower_Center12"] = {
    ["AbandonedTower_Center9"] = function()
      return true
    end,
    ["AbandonedTower_Center10_Shortcut"] = function()
      return true
    end,
    ["AbandonedTower_North1"] = function()
      return true
    end
  },
  ["AbandonedTower_North1"] = {
    ["AbandonedTower_Center12"] = function()
      return true
    end,
    ["AbandonedTower_North2"] = function()
      return true
    end
  },
  ["AbandonedTower_North2"] = {
    ["AbandonedTower_North1"] = function()
      return true
    end,
    ["AbandonedTower_North3"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end,
    ["AbandonedTower_North4"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility()
      })
    end
  },
  ["AbandonedTower_North3"] = {
    ["AbandonedTower_North2"] = function()
      return true
    end,
    ["AbandonedTower_North5"] = function()
      return true
    end
  },
  ["AbandonedTower_North4"] = {
    ["AbandonedTower_North2"] = function()
      return true
    end
  },
  ["AbandonedTower_North5"] = {
    ["AbandonedTower_North3"] = function()
      return true
    end,
    ["AbandonedTower_North6"] = function()
      return true
    end
  },
  ["AbandonedTower_North6"] = {
    ["AbandonedTower_North5"] = function()
      return true
    end,
    ["AbandonedTower_North7"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end,
    ["AbandonedTower_North8"] = function()
      return
      _OR({
        double_jump(),
        improved_flying(),
        dual_mobility(),
        lofty_mount(),
        summon_big_rock()
      })
    end
  },
  ["AbandonedTower_North7"] = {
    ["AbandonedTower_North6"] = function()
      return true
    end
  },
  ["AbandonedTower_North8"] = {
    ["AbandonedTower_North6"] = function()
      return true
    end,
    ["AbandonedTower_North9"] = function()
      return
      _OR({
        double_jump(),
        distant_ledges(),
        summon_big_rock()
      })
    end,
    ["AbandonedTower_NorthHidden"] = function()
      return breakable_walls()
    end
  },
  ["AbandonedTower_North9"] = {
    ["AbandonedTower_North8"] = function()
      return true
    end,
    ["AbandonedTower_Final"] = function()
      return true
    end
  },
  ["AbandonedTower_NorthHidden"] = {
    ["AbandonedTower_North8"] = function()
      return true
    end
  },
  ["AbandonedTower_Final"] = {
    ["AbandonedTower_North9"] = function()
      return true
    end
  },
}
