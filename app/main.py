lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}
all_vars = {
    name: value
    for name, value in globals().items()
    if not name.startswith('_') and name != 'sorted_variables'
}

# Разделение на mutable и immutable
sorted_variables = {
    "mutable": [],
    "immutable": []
}

for var_name, var in all_vars.items():
    if isinstance(var, (list, dict, set)):  # Mutable-типы
        sorted_variables["mutable"].append(var_name)
    elif isinstance(var, (int, float, str, bool, tuple)):  # Immutable-типы
        sorted_variables["immutable"].append(var_name)
