def create_dictionary(*args):
    valid_types = (int, float, str, bool, type(None), tuple)
    dic = {}

    for index, arg in enumerate(args):
        # Verifica se é função (callable) ou tipo permitido e que seja *hashável*
        if isinstance(arg, valid_types) or callable(arg):
            dic[arg] = index
        else:
            print(f"Cannot add {arg} to the dict!")

    return dic
