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

global_vars_snapshot = dict(globals())

mutable_variables = []
immutable_variables = []

for var_name, var_value in global_vars_snapshot.items():
    if var_name != "sorted_variables" and not var_name.startswith("__"):
        if isinstance(var_value, (list, dict, set)):
            mutable_variables.append(var_value)
        else:
            immutable_variables.append(var_value)

sorted_variables = {
    "mutable": [my_favourite_films, marks, collection_of_coins],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info]
}

print(sorted_variables)
