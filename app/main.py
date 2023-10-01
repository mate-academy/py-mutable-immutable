def sort_variables(*args) -> dict:
    sorted_variables = {"mutable": [], "immutable": []}

    for arg in args:
        if isinstance(arg, (list, dict, set)):
            sorted_variables["mutable"].append(arg)
        else:
            sorted_variables["immutable"].append(arg)

    return sorted_variables
