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

mutable_types = (list, dict, set, bytearray)
helper_names = {"mutable_types", "sorted_variables", "user_variables"}

sorted_variables = {
    "mutable": [],
    "immutable": []
}

variables = {
    name: value for name, value in globals().items()
    if not name.startswith("__") and name not in helper_names
}

for value in variables.values():
    if isinstance(value, mutable_types):
        sorted_variables["mutable"].append(value)
    else:
        sorted_variables["immutable"].append(value)
