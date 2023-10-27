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

mutable_vars = []
immutable_vars = []

variables_to_check = [lucky_number, pi, one_is_a_prime_number, name,
                      my_favourite_films, profile_info,
                      marks, collection_of_coins]

for variable_to_check in variables_to_check :
    if isinstance(variable_to_check, (list, dict, set)):
        mutable_vars.append(variable_to_check)
    else:
        immutable_vars.append(variable_to_check)

sorted_variables = {
    "mutable": mutable_vars,
    "immutable": immutable_vars
}

print(sorted_variables)
