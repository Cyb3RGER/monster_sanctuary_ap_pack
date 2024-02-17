function has_access_to(region_name)
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
    local value = 0
    if not REGIONS[region_name] then
        return false
    end
    for k, v in pairs(REGIONS[region_name]) do
        local exit_func_return = v()
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
    return
end

function update_access()
    local start = get_start_location()
    REGIONS_ACCESS_CACHE[start] = true
    _update_access(start, {})
end
