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

for var in [lucky_number, pi, one_is_a_prime_number, name, my_favourite_films, profile_info, marks, collection_of_coins]:
    if isinstance(var, (list, dict, set)):
        mutable_vars.append(var)
    else:
        immutable_vars.append(var)

sorted_variables = {
    "mutable": mutable_vars,
    "immutable": immutable_vars
}

print(sorted_variables)
