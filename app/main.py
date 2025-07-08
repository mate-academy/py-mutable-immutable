
lucky_number = 777
pi_number = 3.14
pi = pi_number
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

variables_type = {
    "lucky_number": lucky_number,
    "pi": pi_number,
    "one_is_a_prime_number": one_is_a_prime_number,
    "name": name,
    "my_favourite_films": my_favourite_films,
    "profile_info": profile_info,
    "marks": marks,
    "collection_of_coins": collection_of_coins
}
mutable = []
immutable = []

for key, variable_type in variables_type.items():
    if isinstance(variable_type, (list, dict, set)):
        mutable.append(variable_type)
    else:
        immutable.append(variable_type)

sorted_variables = {
    "mutable": mutable,
    "immutable": immutable
}
