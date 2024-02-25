function has_access_to(region_name)
    if not IS_CACHED and not REGIONS_ACCESS_CACHE[region_name] then
        -- we called has_access_to on a location where access *might* have not been evaluated yet
        -- we keep track of those and run update those on the existing cache
        if AUTOTRACKER_ENABLE_DEBUG_LOGGING_ACCESS then
            print(string.format("called has_access_to: !NOT CACHED YET! region_name: %s", region_name))
        end
        table.insert(RECACHE_CANDIATES, region_name)
        return false
    end
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_ACCESS then
        print(string.format("called has_access_to: region_name: %s: %s", region_name, REGIONS_ACCESS_CACHE[region_name] or false))
    end
    return REGIONS_ACCESS_CACHE[region_name] or false
end

function get_start_location()
    return 'MountainPath_North1'
end

function _update_access(region_name, checked_regions)
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_ACCESS then
        print(string.format("called _update_access: region_name: %s", region_name))
        -- print(string.format("current cache: %s", dump_table(REGIONS_ACCESS_CACHE)))
    end
    if not REGIONS[region_name] then
        return false
    end
    for k, v in pairs(REGIONS[region_name]) do
        local exit_func_return = REGIONS_ACCESS_CACHE[k] or v()
        if AUTOTRACKER_ENABLE_DEBUG_LOGGING_ACCESS then
            if exit_func_return == nil then
                print(string.format("\t exits function has no return value: region_name: %s -> k: %s", region_name, k))
            end
            print(string.format("\t region_name: %s -> k: %s, v(): %s", region_name, k, exit_func_return))
        end
        if exit_func_return then
            local already_checked = false
            for _, region in pairs(checked_regions) do
                if region == k then
                    already_checked = true
                end
            end
            if not already_checked then
                table.insert(checked_regions, region_name)
                if AUTOTRACKER_ENABLE_DEBUG_LOGGING_ACCESS then
                    print(string.format("\t access from %s to %s", region_name, k))
                end
                REGIONS_ACCESS_CACHE[k] = true
                _update_access(k, checked_regions)
            else
                if AUTOTRACKER_ENABLE_DEBUG_LOGGING_ACCESS then
                    print(string.format("\t already checked; %s: %s", region_name,
                        REGIONS_ACCESS_CACHE[k]))
                end
            end
        end
    end
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_ACCESS then
        print(string.format("\t deadend returning 0; region_name: %s, checked_regions: %s", region_name,
            #checked_regions))
    end
end

IS_CACHED = false
RECACHE_CANDIATES = {}

function update_access()
    RECACHE_CANDIATES = {}
    IS_CACHED = false
    local start = get_start_location()
    REGIONS_ACCESS_CACHE[start] = true
    _update_access(start, {})
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_ACCESS then
        print(string.format("called update_access: #REGIONS_ACCESS_CACHE: %s, #RECACHE_CANDIATES: %s",
            #REGIONS_ACCESS_CACHE, #RECACHE_CANDIATES))
    end
    --ToDo: optimize!
    local recache_counter = 0
    local last_recache_cnt = 0
    --rerun until when don't reach any new locations
    while #RECACHE_CANDIATES > 0 and last_recache_cnt ~= #RECACHE_CANDIATES do
        recache_counter = recache_counter + 1
        last_recache_cnt = #RECACHE_CANDIATES
        RECACHE_CANDIATES = {}
        _update_access(start, {})
    end
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_ACCESS then
        print(string.format("after recache: recache_counter: %s, #RECACHE_CANDIATES: %s", recache_counter,
            dump_table(RECACHE_CANDIATES)))
    end
    IS_CACHED = true
end
