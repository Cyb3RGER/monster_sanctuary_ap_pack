--ToDo: remove this as soon as all items are tracked via AP

function update_access_watch(code)
    REGIONS_ACCESS_CACHE = {}
    print('called update_access_watch', code, update_access)
    update_access()
end

ScriptHost:AddWatchForCode("Update access", "*", update_access_watch)
