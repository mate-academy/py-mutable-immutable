def create_dictionary(*args) -> int:
    dic = {}
    for index, arg in enumerate(args):
        if (isinstance(arg, (int, float, str, bool, type(None), tuple))
            or callable(arg)):
            dic[arg] = index
        else:
            print(f"Cannot add {arg} to the dict!")
    return dic
