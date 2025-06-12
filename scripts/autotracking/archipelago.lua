-- this is an example/ default implementation for AP autotracking
-- it will use the mappings defined in item_mapping.lua and location_mapping.lua to track items and locations via thier ids
-- it will also load the AP slot data in the global SLOT_DATA, keep track of the current index of on_item messages in CUR_INDEX
-- addition it will keep track of what items are local items and which one are remote using the globals LOCAL_ITEMS and GLOBAL_ITEMS
-- this is useful since remote items will not reset but local items might
require("scripts/autotracking/item_mapping")
require("scripts/autotracking/location_mapping")
require("scripts/autotracking/datastorage_mapping")
require("scripts/autotracking/autoswitch_mapping")
require('logic/abilities_compact')
require('logic/monsters_to_abilities')

-- used for hint tracking to quickly map hint status to a value from the Highlight enum
HINT_STATUS_MAPPING = {}
if Highlight then
    HINT_STATUS_MAPPING = {
        [20] = Highlight.Avoid,
        [40] = Highlight.None,
        [10] = Highlight.NoPriority,
        [0] = Highlight.Unspecified,
        [30] = Highlight.Priority,
    }
end

CUR_INDEX = -1
SLOT_DATA = nil
LOCAL_ITEMS = {}
GLOBAL_ITEMS = {}
REGIONS_ACCESS_CACHE = {}
--update_access()

function GetDataStorageKeys()
    local keys = {}
    for k, _ in pairs(DATASTORAGE_ITEM_MAPPING) do
        table.insert(keys, "Slot:" .. Archipelago.PlayerNumber .. ":" .. k)
    end
    table.insert(keys, "Slot:" .. Archipelago.PlayerNumber .. ":" .. "CurrentArea")
    table.insert(keys, GetHintDataStorageKey())
    return keys
end

-- gets the data storage key for hints for the current player
-- returns nil when not connected to AP
function GetHintDataStorageKey()
    if AutoTracker:GetConnectionState("AP") ~= 3 or Archipelago.TeamNumber == nil or Archipelago.TeamNumber == -1 or Archipelago.PlayerNumber == nil or Archipelago.PlayerNumber == -1 then
        if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
            print("Tried to call getHintDataStorageKey while not connect to AP server")
        end
        return nil
    end
    return string.format("_read_hints_%s_%s", Archipelago.TeamNumber, Archipelago.PlayerNumber)
end

function onClear(slot_data)
    Tracker.BulkUpdate = true
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
        print(string.format("called onClear, slot_data:\n%s", dump_table(slot_data)))
    end
    REGIONS_ACCESS_CACHE = {}
    SLOT_DATA = slot_data
    CUR_INDEX = -1
    -- reset locations
    for _, v in pairs(LOCATION_MAPPING) do
        if v[1] then
            if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
                print(string.format("onClear: clearing location %s", v[1]))
            end
            local obj = Tracker:FindObjectForCode(v[1])
            if obj then
                if v[1]:sub(1, 1) == "@" then
                    obj.AvailableChestCount = obj.ChestCount
                else
                    obj.Active = false
                end
            elseif AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
                print(string.format("onClear: could not find object for code %s", v[1]))
            end
        end
    end
    -- reset items
    for _, v in pairs(ITEM_MAPPING) do
        if v[1] and v[2] then
            for _, code in ipairs(v[1]) do
                resetItem(code, v[2])
            end
        end
    end
    for _, v in pairs(DATASTORAGE_ITEM_MAPPING) do
        if v[1] and v[2] then
            for _, code in ipairs(v[1]) do
                resetItem(code, v[2])
            end
        end
    end
    LOCAL_ITEMS = {}
    GLOBAL_ITEMS = {}
    local keys = GetDataStorageKeys()
    Archipelago:Get(keys)
    Archipelago:SetNotify(keys)
    --update_access()
    local obj = Tracker:FindObjectForCode('mozzie')
    if obj then
        if SLOT_DATA.options.goal == 3 then
            obj.MaxCount = SLOT_DATA.options.mozzie_pieces
        else
            obj.MaxCount = 1
        end
    end
    update_access()
    reset_abilities()
    local obj = Tracker:FindObjectForCode('dummy')
    if obj then
        obj.Active = not obj.Active
    end
    Tracker.BulkUpdate = false
end

function resetItem(code, type)
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
        print(string.format("onClear: clearing item %s of type %s", code, type))
    end
    local obj = Tracker:FindObjectForCode(code)
    if obj then
        if type == "toggle" then
            obj.Active = false
        elseif type == "progressive" then
            obj.CurrentStage = 0
            obj.Active = false
        elseif type == "consumable" then
            obj.AcquiredCount = 0
        elseif AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
            print(string.format("onClear: unknown item type %s for code %s", v[2], code))
        end
    elseif AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
        print(string.format("onClear: could not find object for code %s", code))
    end
end

-- called when an item gets collected
function onItem(index, item_id, item_name, player_number)
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
        print(string.format("called onItem: %s, %s, %s, %s, %s", index, item_id, item_name, player_number, CUR_INDEX))
    end
    if not AUTOTRACKER_ENABLE_ITEM_TRACKING then
        return
    end
    if index <= CUR_INDEX then
        return
    end
    local is_local = player_number == Archipelago.PlayerNumber
    CUR_INDEX = index;
    local v = ITEM_MAPPING[item_id]
    if not v then
        if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
            print(string.format("onItem: could not find item mapping for id %s", item_id))
        end
        return
    end
    if not v[1] then
        return
    end
    for _, code in ipairs(v[1]) do
        if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
            print(string.format("onItem: code: %s, type %s", code, v[2]))
        end
        local obj = Tracker:FindObjectForCode(code)
        if obj then
            if v[2] == "toggle" then
                obj.Active = true
            elseif v[2] == "progressive" then
                if obj.Active then
                    obj.CurrentStage = obj.CurrentStage + 1
                else
                    obj.Active = true
                end
            elseif v[2] == "consumable" then
                obj.AcquiredCount = obj.AcquiredCount + obj.Increment
            elseif AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
                print(string.format("onItem: unknown item type %s for code %s", v[2], code))
            end
        elseif AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
            print(string.format("onItem: could not find object for code %s", code))
        end
    end
    -- track local items via snes interface
    if is_local then
        if LOCAL_ITEMS[item_name] then
            LOCAL_ITEMS[item_name] = LOCAL_ITEMS[item_name] + 1
        else
            LOCAL_ITEMS[item_name] = 1
        end
    else
        if GLOBAL_ITEMS[item_name] then
            GLOBAL_ITEMS[item_name] = GLOBAL_ITEMS[item_name] + 1
        else
            GLOBAL_ITEMS[item_name] = 1
        end
    end
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
        print(string.format("local items: %s", dump_table(LOCAL_ITEMS)))
        print(string.format("global items: %s", dump_table(GLOBAL_ITEMS)))
    end
    --update_access()
end

-- called when a location gets cleared
function onLocation(location_id, location_name)
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
        print(string.format("called onLocation: %s, %s", location_id, location_name))
    end
    if not AUTOTRACKER_ENABLE_LOCATION_TRACKING then
        return
    end
    local v = LOCATION_MAPPING[location_id]
    if not v and AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
        print(string.format("onLocation: could not find location mapping for id %s", location_id))
        return
    end
    if not v[1] then
        return
    end
    local obj = Tracker:FindObjectForCode(v[1])
    if obj then
        if v[1]:sub(1, 1) == "@" then
            obj.AvailableChestCount = obj.AvailableChestCount - 1
        else
            obj.Active = true
        end
    elseif AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
        print(string.format("onLocation: could not find object for code %s", v[1]))
    end
    --update_access()
end

function onDataStorageUpdate(key, value, old_value)
    print('onDataStorageUpdate', key, value, old_value)
    if old_value == nil or old_value ~= value then
        if string.find(key, "CurrentArea") then
            updateMapTabFromDataStorage(key, value)
        elseif key == GetHintDataStorageKey() then
            onHintsUpdate(value)
        else
            updateItemsFromDataStorage(key, value)
        end
    end
end

function updateMapTabFromDataStorage(key, value)
    if Tracker:FindObjectForCode("auto_tab").CurrentStage == 0 then
        return
    end
    local split_key = split(key, ':')
    if #split_key ~= 3 then
        return
    end
    if split_key[3] ~= "CurrentArea" then
        return
    end
    local tab = MAP_SWITCHING_MAPPING[value]
    if tab then
        Tracker:UiHint("ActivateTab", tab)
    end
end

function updateItemsFromDataStorage(key, value)
    if value == nil then
        return
    end
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
        print(string.format("updateFromDataStorage: %s, %s, %s", key, value, type(value)))
    end
    local split_key = split(key, ':')
    if #split_key ~= 3 then
        return
    end
    local mapping = DATASTORAGE_ITEM_MAPPING[split_key[3]]
    if not mapping then
        return
    end
    if not mapping[1] then
        return
    end
    local type = mapping[2]
    for _, code in ipairs(mapping[1]) do
        local obj = Tracker:FindObjectForCode(code)
        if obj == nil then
            return
        end
        if code:sub(1, 1) == "@" then
            obj.AvailableChestCount = obj.ChestCount - value
        else
            if type == "toggle" then
                obj.Active = value
            elseif type == "progressive" then
                if obj.Active then
                    obj.CurrentStage = value
                else
                    obj.Active = value
                end
            elseif type == "consumable" then
                obj.AcquiredCount = value
            end
        end
    end
    --update_access()
end

-- called whenever the hints key in data storage updated
function onHintsUpdate(hints)
    -- Highlight is only supported since version 0.32.0
    if PopVersion < "0.32.0" or not AUTOTRACKER_ENABLE_LOCATION_TRACKING then
        return
    end
    local player_number = Archipelago.PlayerNumber
    -- get all new highlight values per section
    local sections_to_update = {}
    for _, hint in ipairs(hints) do
        -- we only care about hints in our world
        if hint.finding_player == player_number then
            updateHint(hint, sections_to_update)
        end
    end
    -- update the sections
    for location_code, highlight_code in pairs(sections_to_update) do
        -- find the location object
        local obj = Tracker:FindObjectForCode(location_code)
        -- check if we got the location and if it supports Highlight
        if obj and obj.Highlight then
            obj.Highlight = highlight_code
        end
    end
end

-- update section highlight based on the hint
function updateHint(hint, sections_to_update)
    -- get the highlight enum value for the hint status
    local hint_status = hint.status
    local highlight_code = nil
    if hint_status then
        highlight_code = HINT_STATUS_MAPPING[hint_status]
    end
    if not highlight_code then
        if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
            print(string.format("updateHint: unknown hint status %s for hint on location id %s", hint.status,
                hint.location))
        end
        -- try to "recover" by checking hint.found (older AP versions without hint.status)
        if hint.found == true then
            highlight_code = Highlight.None
        elseif hint.found == false then
            highlight_code = Highlight.Unspecified
        else
            return
        end
    end
    -- get the location mapping for the location id
    local mapping_entry = LOCATION_MAPPING[hint.location]
    if not mapping_entry then
        if AUTOTRACKER_ENABLE_DEBUG_LOGGING_AP then
            print(string.format("updateHint: could not find location mapping for id %s", hint.location))
        end
        return
    end
    --get the "highest" highlight value pre section
    for _, location_code in pairs(mapping_entry) do
        -- skip hosted items, they don't support Highlight
        if location_code and location_code:sub(1, 1) == "@" then
            -- see if we already set a Highlight for this section
            local existing_highlight_code = sections_to_update[location_code]
            if existing_highlight_code then
                -- make sure we only replace None or "increase" the highlight but never overwrite with None
                -- this so sections with mulitple mapped locations show the "highest" Highlight and
                -- only show no Highlight when all hints are found
                if existing_highlight_code == Highlight.None or (existing_highlight_code < highlight_code and highlight_code ~= Highlight.None) then
                    sections_to_update[location_code] = highlight_code
                end
            else
                sections_to_update[location_code] = highlight_code
            end
        end
    end
end

-- add AP callbacks
-- un-/comment as needed
Archipelago:AddClearHandler("clear handler", onClear)
if AUTOTRACKER_ENABLE_ITEM_TRACKING then
    Archipelago:AddItemHandler("item handler", onItem)
    Archipelago:AddRetrievedHandler("item handler", onDataStorageUpdate)
    Archipelago:AddSetReplyHandler("item handler", onDataStorageUpdate)
end
if AUTOTRACKER_ENABLE_LOCATION_TRACKING then
    Archipelago:AddLocationHandler("location handler", onLocation)
end
