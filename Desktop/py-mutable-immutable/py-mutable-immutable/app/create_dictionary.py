from typing import Any, Dict


def create_dictionary(*args: Any) -> Dict[Any, int]:
    result: Dict[Any, int] = {}
    for index, arg in enumerate(args):
        if (
            isinstance(arg, (int, float, str, bool, type(None), tuple))
            or callable(arg)
        ):
            result[arg] = index
        else:
            print(f"Cannot add {arg} to the dict!")
    return result


