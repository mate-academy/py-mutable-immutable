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

sorted_variables = {
    "mutable": [],
    "immutable": []
}

for var_name in dir():
    if not var_name.startswith("__"):
        variable_value = eval(var_name)
        if isinstance(variable_value, (list, dict, set)):
            sorted_variables["mutable"].append(variable_value)
        else:
            sorted_variables["immutable"].append(variable_value)

print(sorted_variables)
