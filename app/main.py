def sorted_variables(*args) -> dict:
    result = {}
    mutable = []
    immutable = []
    for i in args:
        if isinstance(i, (list, dict, set)):
            mutable.append(i)
        else:
            immutable.append(i)
    result["mutable"] = mutable
    result["immutable"] = immutable
    return result
