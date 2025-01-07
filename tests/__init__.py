a = [1, 2]


def variables(text):
    sorted_variables = {}
    mutable = []
    immutable = []
    if isinstance(text, (str, float, int ,bool, tuple)):
        immutable.append(text)
    if isinstance(text, (list, dict, set)):
        mutable.append(text)
    sorted_variables = {"mutable": mutable,"immutable": immutable}
    return sorted_variables
print(variables(a))
