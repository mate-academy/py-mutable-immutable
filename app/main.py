import types


def categorize_variables() -> str:
    mutable_types = [list, set, dict]
    immutable_types = [int, float, str, bool, tuple]
    sorted_variables = {"mutable": [], "immutable": []}
    main_module = types.ModuleType("__main__")
    main_vars = vars(main_module)
    for var_name, var_value in main_vars.items():
        if any(isinstance(var_value, t) for t in mutable_types):
            sorted_variables["mutable"].append(var_value)
        elif any(isinstance(var_value, t) for t in immutable_types):
            sorted_variables["immutable"].append(var_value)

    return sorted_variables
