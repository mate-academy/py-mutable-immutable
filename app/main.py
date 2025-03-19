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

# def sorted_variables(**kwargs):
#     for key, value in kwargs.items():
#         if value == int and value == float and value == bool:
#             sorted_variables['immutable'] = list(value)
#         else:
#             sorted_variables['mutable'] = list(value)

sorted_variables = {"mutable": [], "immutable": []}
for value in sorted_variables:
    if isinstance(value, (int, float, str, tuple, frozenset, bool)):
        sorted_variables["immutable"].append(value)
    else:
        sorted_variables["mutable"].append(value)
