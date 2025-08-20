a = 123 # immutable
b = []  # mutable
c = "Hi!"  # immutable
d = 3.14 # immutable
e = {2, 4, 6} # mutable
f ={"tg": 1, "tr": "good"}  # mutable
g = ("a", "b", "c") # immutable
h = bytearray(c"Hello")  # mutable

sorted_variables = {
    "mutable": [b, e, f, h],
    "immutable": [a, c, d, g]
}
