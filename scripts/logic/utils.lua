function _AND(args)
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_UTILS then
        print(string.format("called _AND: args %s", args))
    end
    if type(args) == 'boolean' then
        return args
    end
    local result = true
    for i = 1, #args do
        if not result then
            break
        end
        if AUTOTRACKER_ENABLE_DEBUG_LOGGING_UTILS then
            print(string.format("\targs[i]: %s, result: %s", args[i], result))
        end
        result = result and args[i]
    end
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_UTILS then
        print(string.format("\t\tresult: %s", result))
    end
    return result
end

function _OR(args)
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_UTILS then
        print(string.format("called _OR: args %s, type(args) %s", args, type(args)))
    end
    if type(args) == 'boolean' then
        print(args[1])
        return args
    end
    local result = false
    for i = 1, #args do
        if result then
            break
        end
        if AUTOTRACKER_ENABLE_DEBUG_LOGGING_UTILS then
            print(string.format("\targs[i]: %s, result: %s", args[i], result))
        end
        result = result or args[i]
    end
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_UTILS then
        print(string.format("\t\tresult: %s", result))
    end
    return result
end

function _NOT(arg)
    return not arg
end

function _NOT_CALL(func_name)
    if AUTOTRACKER_ENABLE_DEBUG_LOGGING_UTILS then
        print(string.format("_NOT_CALL: %s, %s, %s", func_name, _G[func_name], _G[func_name]()))
    end
    -- return false
    return not _G[func_name]()
end

function has(code, amount)
    if amount == nil then
        amount = 1
    end
    return Tracker:ProviderCountForCode(code) >= amount
end

function has_all(req_table)
	local tmp = {}
	for _, value in ipairs(req_table) do
	    table.insert(tmp, has(value.Code, value.Amount))
	end
	return _AND(tmp)
end
