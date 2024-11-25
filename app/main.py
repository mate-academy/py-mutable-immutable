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

# Ініціалізація словника для результатів
sorted_variables = {
    "mutable": [],
    "immutable": [],
}

# Перевірка кожної змінної та її типу
variables = {
    "lucky_number": lucky_number,
    "pi": pi,
    "one_is_a_prime_number": one_is_a_prime_number,
    "name": name,
    "my_favourite_films": my_favourite_films,
    "profile_info": profile_info,
    "marks": marks,
    "collection_of_coins": collection_of_coins,
}

for var_name, var_value in variables.items():
    if isinstance(var_value, (int, float, bool, str, tuple)):
        sorted_variables["immutable"].append(var_value)
    elif isinstance(var_value, (list, dict, set)):
        sorted_variables["mutable"].append(var_value)