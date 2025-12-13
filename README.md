g = {"x": 1}
h = True
i = 3.14

e = (1, 2, 3)       # tuple → immutable
f = {1, 2, 3}       # set → mutable
g = {"x": 1}        # dict → mutable
h = True            # bool → immutable
i = 3.14            # float → immutable

sorted_variables = {
    "mutable": [b, d, f, g],
    "immutable": [a, c, e, h, i],
}
sorted_variables = sorted([
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i"
])