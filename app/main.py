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
for var_name, var_value in locals().items():
    if isinstance(var_value, (list, dict, set)):
        sorted_variables["mutable"].append(var_value)
    else:
        sorted_variables["immutable"].append(var_value)

# Output the sorted variables
print(sorted_variables)
