-- this is an example/ default implementation for AP autotracking
-- it will use the mappings defined in item_mapping.lua and location_mapping.lua to track items and locations via thier ids
-- it will also load the AP slot data in the global SLOT_DATA, keep track of the current index of on_item messages in CUR_INDEX
-- addition it will keep track of what items are local items and which one are remote using the globals LOCAL_ITEMS and GLOBAL_ITEMS
-- this is useful since remote items will not reset but local items might
require("scripts/autotracking/item_mapping")
require("scripts/autotracking/location_mapping")
require("scripts/autotracking/datastorage_mapping")
require("scripts/autotracking/autoswitch_mapping")

CUR_INDEX = -1
SLOT_DATA = nil
LOCAL_ITEMS = {}
GLOBAL_ITEMS = {}
REGIONS_ACCESS_CACHE = {}
--update_access()

function GetDataStorageKeys()
    local keys = {}
    for k, _ in pairs(DATASTORAGE_ABILITY_MAPPING) do
        table.insert(keys, "Slot:" .. Archipelago.PlayerNumber .. ":" .. k)
    end
    table.insert(keys, "Slot:" .. Archipelago.PlayerNumber .. ":" .. "CurrentArea")
    return keys
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
    for _, v in pairs(DATASTORAGE_ABILITY_MAPPING) do
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

function onRetrieved(key, value)
    if string.find(key, "CurrentArea") then
        updateMapTabFromDataStorage(key, value)
    else
        updateItemsFromDataStorage(key, value)
    end
end

function onSetReply(key, value, old_value)
    if old_value ~= value then
        if string.find(key, "CurrentArea") then
            updateMapTabFromDataStorage(key, value)
        else
            updateItemsFromDataStorage(key, value)
        end
    end
end

function updateMapTabFromDataStorage(key, value)
    if value == nil then
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
    local mapping = DATASTORAGE_ABILITY_MAPPING[split_key[3]]
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

-- add AP callbacks
-- un-/comment as needed
Archipelago:AddClearHandler("clear handler", onClear)
if AUTOTRACKER_ENABLE_ITEM_TRACKING then
    Archipelago:AddItemHandler("item handler", onItem)
    Archipelago:AddRetrievedHandler("item handler", onRetrieved)
    Archipelago:AddSetReplyHandler("item handler", onSetReply)
end
if AUTOTRACKER_ENABLE_LOCATION_TRACKING then
    Archipelago:AddLocationHandler("location handler", onLocation)
end
