DEBUG_MODE = false
ENABLE_DEBUG_LOG = false or DEBUG_MODE
DEBUG = false

if Tracker.AllowDeferredLogicUpdate == false then
    Tracker.AllowDeferredLogicUpdate = true
end

local variant = Tracker.ActiveVariantUID
IS_ITEMS_ONLY = variant:find("itemsonly")

print("-- Monster Sanctuary AP Tracker --")
print("Loaded variant: ", variant)
if ENABLE_DEBUG_LOG then
    print("Debug logging is enabled!")
end

-- Utility Script for helper functions etc.
require("scripts/utils")

-- Logic
require("scripts/logic/logic")

-- Items
Tracker:AddItems("items/abilities.json")
Tracker:AddItems("items/catalyst.json")
Tracker:AddItems("items/crafting_material.json")
Tracker:AddItems("items/egg.json")
Tracker:AddItems("items/flag.json")
Tracker:AddItems("items/key_item.json")
Tracker:AddItems("items/monsters.json")
Tracker:AddItems("items/explore_ability.json")
Tracker:AddItems("items/eggsanity.json")
Tracker:AddItems("items/rank.json")
Tracker:AddItems("items/other.json")


if not IS_ITEMS_ONLY then
    -- Maps
    Tracker:AddMaps("maps/maps.json")
    -- Locations
    if DEBUG_MODE then
        Tracker:AddLocations("locations/debug.json")
    else
        Tracker:AddLocations("locations/locations.json")
    end
end

-- Layout
Tracker:AddLayouts("layouts/generated/eggsanity.json")
Tracker:AddLayouts("layouts/items.json")
Tracker:AddLayouts("layouts/tracker.json")
Tracker:AddLayouts("layouts/broadcast.json")

-- AutoTracking for Poptracker
if PopVersion and PopVersion >= "0.18.0" then
    require("scripts/autotracking")
    require("scripts/watches")
end
