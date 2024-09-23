a = 123
b = []
c = "Hi!"
d = [1, 2]

variables = [
    a,
    b,
    c,
    d
]
sorted_variables = {
    "mutable": [],
    "immutable": [],
}

for current_variable in variables:
    if isinstance(current_variable, (list, dict, set)):
        sorted_variables["mutable"].append(current_variable)
    else:
        sorted_variables["immutable"].append(current_variable)

print(sorted_variables)
