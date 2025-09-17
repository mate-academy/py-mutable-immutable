# app/main.py

# 1. Declaração das 8 variáveis, conforme a tarefa.
# Tipos Imutáveis
var_int = 10
var_float = 3.14
var_str = "Kodree"
var_tuple = (1, 2, 3)
var_bool = True

# Tipos Mutáveis
var_list = [1, 2, 3]
var_dict = {"key": "value"}
var_set = {1, 2, 3}

# 2. Agrupar as 8 variáveis em uma lista.
all_variables = [
    var_int, var_float, var_str, var_tuple,
    var_bool, var_list, var_dict, var_set
]

# 3. Definir os tipos mutáveis.
MUTABLE_TYPES = (list, dict, set, bytearray)

# 4. Inicializar o dicionário de saída.
sorted_variables = {
    "mutable": [],
    "immutable": []
}

# 5. Iterar e classificar as variáveis.
for item in all_variables:
    if isinstance(item, MUTABLE_TYPES):
        sorted_variables["mutable"].append(item)
    else:
        sorted_variables["immutable"].append(item)
