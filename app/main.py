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
    "mutable": [collection_of_coins, marks, my_favourite_films],
    "immutable": [profile_info, name, one_is_a_prime_number, pi, lucky_number]
}


# def sorted_variables_def(*args, **kwargs) -> dict:
#     sorted_variables = {}
#     name_mutable_variables = []
#     name_immutable_variables = []
#
#     for i in args:
#         if isinstance(i, (list, set, dict)):
#             name_mutable_variables.append(i)
#         else:
#             name_immutable_variables.append(i)
#     sorted_variables["mutable"] = name_mutable_variables
#     sorted_variables["immutable"] = name_immutable_variables
#     return sorted_variables
#
#
# sorted_variables_def(
#     lucky_number, pi, one_is_a_prime_number
# )
