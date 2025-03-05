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

# sorted_variables = {'mutable': [], 'immutable': []}
#
# def mutable_immutable(*var) -> dict:
#     ls_mutable = []
#     ls_immutable = []
#     for i in range(len(var)):
#         for name, val in globals().items():
#             if val == var[i]:
#                 break
#         if type(val) == list or type(val) == set or type(val) == dict:
#             sorted_variables['mutable'].append(name)
#         else:
#             sorted_variables['immutable'].append(name)
#
#     # sorted_variables['mutable'] = ls_mutable
#     # sorted_variables['immutable'] = ls_immutable
#
#     return sorted_variables
#
#
# print(mutable_immutable(lucky_number, pi, one_is_a_prime_number,
#       name, my_favourite_films, profile_info, marks, collection_of_coins))

sorted_variables = {
    "mutable": [my_favourite_films, marks, collection_of_coins],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info]
}
