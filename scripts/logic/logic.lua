require('logic/utils')
require('logic/logic_generated')
require('logic/access')
require('logic/regions')

--alias
double_jump = double_jump_boots
has_dodo = dodo_egg --ToDo: this should really come via DataStorge from the mod I think
post_game = mad_lord_defeated
third_bex_encounter = third_beach_bex
ancient_woods_magma_chamber_shortcut = ancient_woods_magma_chamber_1

--slot_data
function shifting_avialable()
    if SLOT_DATA == nil then
        return false
    end
    return _OR({
        SLOT_DATA.options.monster_shift_rule == 2,
        _AND({
            SLOT_DATA.options.monster_shift_rule == 1,
            sun_palace_raise_center_3()
        })
    })
end
function no_locked_doors()
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.remove_locked_doors == 2
end
function minimal_locked_doors()
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.remove_locked_doors == 1
end
function normal_plot()
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.skip_plot == 0
end
function plotless()
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.skip_plot == 1
end

function is_goal_mad_lord()
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.goal == 0
end

function is_goal_not_mad_lord()
    return not is_goal_mad_lord()
end

--logic helpers
function all_blob_keys_used()
    return _AND({
        stronghold_dungeon_blob_key(),
        sun_palace_blob_key(),
        mystical_workshop_blob_key()
    })
end
function ancient_woods_magma_chamber_shortcut()
    return _AND({
        ancient_woods_magma_chamber_1(),
        ancient_woods_magma_chamber_2()
    })
end
function tar()
    return _OR({
        tar_mount(),
        dual_mobility()
    })
end

--amount helpers
function all_celestial_feathers()
    return celestial_feather(3)
end
function one_blue_cave_key()
    return blue_cave_key(1)
end
function two_blue_cave_keys()
    return blue_cave_key(2)
end
function three_blue_cave_keys()
    return blue_cave_key(3)
end
function one_dungeon_key()
    return stronghold_dungeon_key(1)
end
function two_dungeon_keys()
    return stronghold_dungeon_key(2)
end
function two_ancient_woods_keys()
    return ancient_woods_key(2)
end
function three_ancient_woods_keys()
    return ancient_woods_key(3)
end
function one_magma_chamber_key()
    return magma_chamber_key(1)
end
function two_magma_chamber_keys()
    return magma_chamber_key(2)
end
function three_workshop_keys()
    return mystical_workshop_key(3)
end
function all_sanctuary_tokens()
    return sanctuary_token(5)
end
function all_rare_seashells()
    return rare_seashell(5)
end

--keeper ranks
function keeper_rank_1()
    return champion_defeated(1)
end
function keeper_rank_2()
    return champion_defeated(3)
end
function keeper_rank_3()
    return champion_defeated(5)
end
function keeper_rank_4()
    return champion_defeated(7)
end
function keeper_rank_5()
    return champion_defeated(9)
end
function keeper_rank_6()
    return champion_defeated(12)
end
function keeper_rank_7()
    return champion_defeated(15)
end
function keeper_rank_8()
    return champion_defeated(19)
end
function keeper_rank_9()
    return champion_defeated(27)
end
