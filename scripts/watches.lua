function update_access_watch(code)
    REGIONS_ACCESS_CACHE = {}
    update_access()
end

--ToDo: since we have the list of monster -> ability -> obstactles in python, 
-- we could optimize this by exporting monster -> obstactle list so not every ability gets recalulated
function update_abilites_from_monster(code)
    if not SLOT_DATA or not code then
        return
    end
    local abilites = MONSTERS_TO_ABILITIES[code]
    if not abilites then
        print(string.format('! abilites is null for code %s !', code))
        return
    end
    for _, v in ipairs(abilites) do
        local has_val = has(code)
        local obj = Tracker:FindObjectForCode(v)
        if obj and has_val then
            obj.Active = has_val
        end
        local val = _is_explore_ability_available(code)
        obj = Tracker:FindObjectForCode(v..'_locked')
        if obj and val then
            obj.Active = not val
        end
    end
end

function update_abilites_from_unlock_item(code)
    if not SLOT_DATA then
        return
    end
    for k, v in ipairs(MONSTER_ABILITY_ITEM_DATA) do
        if v.AbilityItem == code or v.SpeciesItem == code or v.TypeItem == code then
            update_abilites_from_monster(k)
        end
    end
end

function reset_abilities()
    for _, v in ipairs(ABILITIES_COMPACT) do
        local val = SLOT_DATA.options.lock_explore_abilities ~= 0
        local obj = Tracker:FindObjectForCode(v)
        if obj then
            obj.Active = false
        end
        local obj = Tracker:FindObjectForCode(v..'_locked')
        if obj then
            obj.Active = val
        end
    end
end

ScriptHost:AddWatchForCode("Update access", "*", update_access_watch)
for k,v in pairs(MONSTER_ABILITY_ITEM_DATA) do
    ScriptHost:AddWatchForCode("Update abilties from "..k, k, update_abilites_from_monster)
    ScriptHost:AddWatchForCode("Update abilties from "..v.AbilityItem, v.AbilityItem, update_abilites_from_unlock_item)
    ScriptHost:AddWatchForCode("Update abilties from "..v.TypeItem, v.TypeItem, update_abilites_from_unlock_item)
    ScriptHost:AddWatchForCode("Update abilties from "..v.SpeciesItem, v.SpeciesItem, update_abilites_from_unlock_item)
end