# app/main.py

# 1. Definição das 8 variáveis EXATAS que os testes esperam.
# Tipos Imutáveis
lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
profile_info = ("michel", "michel@gmail.com", "12345678")

# Tipos Mutáveis
# CORREÇÃO: Atualizando a lista para corresponder aos testes.
my_favourite_films = ["Inception", "The Matrix", "Interstellar"]
marks = {"John": 4, "Sergio": 3}
collection_of_coins = {1, 2, 25}

# 2. Agrupar todas as variáveis em uma lista para a classificação.
all_variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]

# 3. Definir os tipos de dados que são considerados mutáveis.
MUTABLE_TYPES = (list, dict, set, bytearray)

# 4. Inicializar o dicionário de saída com listas vazias.
sorted_variables = {
    "mutable": [],
    "immutable": [],
}

# 5. Iterar sobre cada variável, classificar e adicionar à lista apropriada.
for item in all_variables:
    if isinstance(item, MUTABLE_TYPES):
        sorted_variables["mutable"].append(item)
    else:
        sorted_variables["immutable"].append(item)
