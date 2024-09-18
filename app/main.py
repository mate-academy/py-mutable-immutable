a: int = 123
b: list = []
c: str = "Hi!"
d: list = [1, 2]

sorted_variables = {
    "mutable": [],
    "immutable": []
}

variables = [a, b, c, d]

for var in variables:
    if isinstance(var, (list, dict, set)):
        sorted_variables["mutable"].append(var)
    else:
        sorted_variables["immutable"].append(var)

print(sorted_variables)
