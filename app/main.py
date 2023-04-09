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
# -----------------------------------------------------
mutable_variables = []
immutable_variables = []

for variables in [lucky_number, pi, one_is_a_prime_number,
                  name, my_favourite_films, profile_info,
                  marks, collection_of_coins]:
    if isinstance(variables, (list, dict, set)):
        mutable_variables.append(variables)
    else:
        immutable_variables.append(variables)

sorted_variables = {
    "mutable": mutable_variables,
    "immutable": immutable_variables
}

print(sorted_variables)
