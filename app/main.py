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

user_variables = [
    "lucky_number",
    "pi",
    "one_is_a_prime_number",
    "name",
    "my_favourite_films",
    "profile_info",
    "marks",
    "collection_of_coins"
]
sorted_variables = {"mutable": [], "immutable": []}
for var_name in user_variables:
    var_value = globals()[var_name]
    if isinstance(var_value, (list, dict, set, bytearray)):
        sorted_variables["mutable"].append(var_name)
    elif isinstance(var_value, (int, float, str, tuple, bool, frozenset, bytes)):
        sorted_variables["immutable"].append(var_name)
print(sorted_variables)
