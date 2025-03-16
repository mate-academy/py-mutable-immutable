a = 123
b = []
c = "Hi!"
d = [1, 2]
e = (3, 4) 
f = {"key": "value"} 
g = {1, 2, 3} 
h = 3.14

def is_mutable(obj):
    try:
        obj.__hash__
        return False
    except TypeError:
        return True

sorted_variables = {
    "mutable": [var for var in [a, b, c, d, e, f, g, h] if is_mutable(var)],
    "immutable": [var for var in [a, b, c, d, e, f, g, h] if not is_mutable(var)]
}

print(sorted_variables)
