a = 123          # int 
b = []           # list 
c = "Hi!"        # str 
d = [1, 2]       # list 
e = 3.14         # float 
f = (1, 2, 3)    # tuple 
g = {"key": "value"}  # dict 
h = {1, 2, 3}    # set 

sorted_variables = {
    "mutable": [b, d, g, h],
    "immutable": [a, c, e, f]}

print(sorted_variables)

