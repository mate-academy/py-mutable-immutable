# Given 8 variables of different data types
a = 123  # Immutable (int)
b = []  # Mutable (list)
c = "Hi!"  # Immutable (str)
d = [1, 2]  # Mutable (list)
e = (4, 5)  # Immutable (tuple)
f = {6, 7}  # Mutable (set)
g = {"key": "value"}  # Mutable (dict)
h = 3.14  # Immutable (float)


mutable_list = []
immutable_list = []

# Classifying variables
for var in [a, b, c, d, e, f, g, h]:
    if isinstance(var, (list, dict, set)):  # Mutable types
        mutable_list.append(var)
    else:  # Immutable types
        immutable_list.append(var)

# Creating the dictionary
sorted_variables = {
    "mutable": mutable_list,
    "immutable": immutable_list
}

print(sorted_variables)
