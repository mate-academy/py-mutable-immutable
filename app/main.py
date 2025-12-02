# As 8 variáveis já existentes no módulo principal (exemplo genérico)
a = 10
b = "hello"
c = [1, 2, 3]
d = (4, 5)
e = {"x": 1}
f = 3.14
g = {1, 2, 3}
h = True

# Separando mutáveis e imutáveis
mutable_types = (list, dict, set)
immutable_types = (int, float, str, tuple, bool)

variables = [a, b, c, d, e, f, g, h]

sorted_variables = {
    "mutable": [var for var in variables if isinstance(var, mutable_types)],
    "immutable": [var for var in variables if isinstance(var, immutable_types)]
}

print(sorted_variables)

