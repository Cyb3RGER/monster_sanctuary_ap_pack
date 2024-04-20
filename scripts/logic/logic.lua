require('logic/utils')
require('logic/logic_generated')
require('logic/access')
require('logic/regions')
require('logic/monster_ability_item_data')

--alias
double_jump = double_jump_boots
--has_dodo = dodo_egg --ToDo: this should really come via DataStorge from the mod I think
post_game = mad_lord_defeated
third_bex_encounter = third_beach_bex

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

function skip_plot()
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.skip_plot == 1
end

function open_underworld_entrances()
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.open_underworld == 1
end

function not_open_underworld_entrances()
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.open_underworld ~= 1
end

function is_goal(goal)
    if type(goal) ~= 'number' then
        goal = tonumber(goal)
    end
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.goal == goal
end

function is_not_goal(goal)
    return not is_goal(goal)
end

function is_shopsanity()
    if SLOT_DATA == nil then
        return false
    end
    print('is_shopsanity', SLOT_DATA.locations.shops)
    if SLOT_DATA.locations.shops then
        return true
    end
    return false
end

function not_is_shopsanity()
    return not is_shopsanity()
end

function check_option(option_name, val)
    print('check_option', option_name, val, SLOT_DATA)
    if type(val) ~= 'number' then
        val = tonumber(val)
    end
    if SLOT_DATA == nil then
        return false
    end
    print('check_option (2)', option_name, val, SLOT_DATA.options[option_name])
    return SLOT_DATA.options[option_name] == val
end

function not_check_option(option_name, val)
    return not check_option(option_name, val)
end

function shops_ignore_rank()
    if SLOT_DATA == nil then
        return false
    end
    return SLOT_DATA.options.shops_ignore_rank == 1
end

--logic helpers
function all_blob_keys_used()
    return _OR({
        _AND({
            stronghold_dungeon_blob_key(),
            sun_palace_blob_key(),
            mystical_workshop_blob_key()
        }),
        open_blob_burg(1),
        open_blob_burg(3)
    })
end

function ancient_woods_magma_chamber_shortcut()
    return _OR({
        _AND({
            ancient_woods_magma_chamber_1(),
            ancient_woods_magma_chamber_2()
        }),
        open_magma_chamber(1),
        open_magma_chamber(3),
    })
end

function tar()
    return _OR({
        tar_mount(),
        dual_mobility()
    })
end


function can_use_ability(monster)
    return _AND({
        has_ability(monster),
        is_explore_ability_available(monster)
    })
end


function has_ability(monster)
    for _,v in ipairs(MONSTERS_TO_ABILITIES[monster]) do
        if has(v) then
            return true
        end
    end
    return false
end

function is_explore_ability_available(monster)
    for _,v in ipairs(MONSTERS_TO_ABILITIES[monster]) do
        if not has(v..'_locked') then
            return true
        end
    end
    return false
end

function _is_explore_ability_available(monster)
    if not SLOT_DATA then
        return false
    end
    local opt = SLOT_DATA.options.lock_explore_abilities
    if opt == 0 then
        return true
    end
    if not MONSTER_ABILITY_ITEM_DATA[monster] then
        print(string.format('!! MONSTER_ABILITY_ITEM_DATA for %s is missing !!', monster))
        return false
    end
    if opt == 1 then
        return has(MONSTER_ABILITY_ITEM_DATA[monster].TypeItem)
    end
    if opt == 2 then
        return has(MONSTER_ABILITY_ITEM_DATA[monster].AbilityItem)
    end
    if opt == 3 then
        return has(MONSTER_ABILITY_ITEM_DATA[monster].SpeciesItem)
    end
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
    return sanctuary_token(5) or open_underworld(1) or open_underworld(3)
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
