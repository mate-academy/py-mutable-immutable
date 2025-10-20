from typing import Any, Dict


def create_dictionary(*args) -> Dict[Any, int]:
    dic: Dict[Any, int] = {}
    for index, arg in enumerate(args):
        if (isinstance(arg,(int,float,str,bool,type(None),tuple))
                or callable(arg)):
            try:
                dic[arg] = index
            except TypeError:
                # arg não é hashable (por ex. tuple com lista dentro)
                print(f"Cannot add {arg} to the dict!")
        else:
            print(f"Cannot add {arg} to the dict!")
    return dic
