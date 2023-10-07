def check_type(list_elem : list) -> dict:
    for_mutable = []
    for_immutable = []
    sorted_variables = {}
    for elem in list_elem:
        if isinstance(elem, (int, str, tuple, float)):
            for_immutable.append(elem)
        else:
            for_mutable.append(elem)
    sorted_variables["mutable"] = for_mutable
    sorted_variables["immutable"] = for_immutable
    return sorted_variables

