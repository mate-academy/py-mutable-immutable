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


sorted_variables = {"mutable": [], "immutable" : []}
mutable_types = (list, dict, set)
immutable_types = (int, float, str, bool, tuple)

for var_name, var_value in locals().copy().items():
    if var_name.startswith("__") or var_name in ["sorted_variables",
                                                 "mutable_types",
                                                 "immutable_types"]:
        continue
    if isinstance(var_value, mutable_types):
        sorted_variables["mutable"].append(var_value)
    elif isinstance(var_value, immutable_types):
        sorted_variables["immutable"].append(var_value)
