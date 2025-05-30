require("logic.champion_locs")

function update_access_watch(code)
    REGIONS_ACCESS_CACHE = {}
    update_access()
end

function update_abilites_from_monster(code)
    if not SLOT_DATA or not code then
        return
    end
    local abilites = MONSTERS_TO_ABILITIES[code]
    if abilites == nil then
        print(string.format('! abilites is null for code %s !', code))
        return
    end
    for _, v in ipairs(abilites) do
        local has_val = has(code)
        local obj = Tracker:FindObjectForCode(v)
        if obj then
            if not obj.Active and has_val then
                obj.Active = true
            end
        end
        -- only unlock ability if we have the monster
        -- because otherwise it might be unlocked and collected from two different monsters
        if has_val then
            local val = _is_explore_ability_available(code)
            obj = Tracker:FindObjectForCode(v .. '_locked')
            if obj then
                if obj.Active and val then
                    obj.Active = false
                end
            end
        end
    end
end

function update_abilites_from_unlock_item(code)
    if not SLOT_DATA then
        return
    end
    for k, v in pairs(MONSTER_ABILITY_ITEM_DATA) do
        local prog_data = MONSTER_ABILITY_PROG_DATA[v.Progressive]
        local found = v.Ability == code or v.Species == code or v.Type == code or prog_data.Progressive.Code == code
        if not found then
            for _, v2 in ipairs(prog_data.Combo) do
                if v2.Code == code then
                    found = true
                    break
                end
            end
        end
        if found then
            update_abilites_from_monster(k)
        end
    end
end

function reset_abilities()
    for _, v in ipairs(ABILITIES_COMPACT) do
        local val = (SLOT_DATA.options.lock_explore_abilities or 0) ~= 0
        local obj = Tracker:FindObjectForCode(v)
        if obj then
            obj.Active = false
        end
        local obj = Tracker:FindObjectForCode(v .. '_locked')
        if obj then
            obj.Active = val
        end
    end
end

function update_champions_in_logic()
    local count = 0
    for _, code in ipairs(CHAMPION_LOCS) do
        local section = Tracker:FindObjectForCode(code) ---@cast section LocationSection?
        if section then
            if section.AccessibilityLevel >= AccessibilityLevel.Normal then
                count = count + 1
            end
        end
    end
    local obj = Tracker:FindObjectForCode("champions_in_logic") ---@cast obj JsonItem?
    if obj then
        obj:SetOverlay(string.format("%d", count))
        obj:SetOverlayFontSize(28)
    end
end

ScriptHost:AddWatchForCode("Update access", "*", update_access_watch)
ScriptHost:AddWatchForCode("update champions in logic", "*", update_champions_in_logic)
for k, v in pairs(MONSTER_ABILITY_ITEM_DATA) do
    ScriptHost:AddWatchForCode("Update abilties from " .. k, k, update_abilites_from_monster)
    ScriptHost:AddWatchForCode("Update abilties from " .. v.Ability, v.Ability, update_abilites_from_unlock_item)
    ScriptHost:AddWatchForCode("Update abilties from " .. v.Type, v.Type, update_abilites_from_unlock_item)
    ScriptHost:AddWatchForCode("Update abilties from " .. v.Species, v.Species, update_abilites_from_unlock_item)
    local prog_data = MONSTER_ABILITY_PROG_DATA[v.Progressive]
    ScriptHost:AddWatchForCode("Update abilties from " .. prog_data.Progressive.Code, prog_data.Progressive.Code,
        update_abilites_from_unlock_item)
    for _, v2 in ipairs(prog_data.Combo) do
        ScriptHost:AddWatchForCode("Update abilties from " .. v2.Code, v2.Code, update_abilites_from_unlock_item)
    end
end
