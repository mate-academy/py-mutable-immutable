# Define variables
a = 123
b = []
c = "Hi!"
d = [1, 2]
e = (1, 2, 3)
f = {"name": "John", "age": 30}
g = True
h = {"apple", "banana", "cherry"}

# Initialize the dictionary
sorted_variables = {
    "mutable": [],
    "immutable": []
}

# Sort variables into mutable and immutable categories
for var in [a, b, c, d, e, f, g, h]:
    if isinstance(var, (list, dict, set)):
        sorted_variables["mutable"].append(var)
    else:
        sorted_variables["immutable"].append(var)

# Output the sorted variables
print(sorted_variables)
