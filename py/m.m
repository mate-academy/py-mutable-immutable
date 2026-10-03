a = 42
b = [1, 2, 3]
c = "Python"
d = {"id": 1}
e = 3.14
f = {10, 20}
g = False
h = (5, 6)

todas_as_variaveis = [a, b, c, d, e, f, g, h]

resultado = {
    "imutaveis": [],
    "mutaveis": []
}

tipos_mutaveis = (list, dict, set)

for var in todas_as_variaveis:
    if isinstance(var, tipos_mutaveis):
        resultado["mutaveis"].append(var)
    else:
        resultado["imutaveis"].append(var)

print(resultado)
