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
    'mutable': [my_favourite_films, marks, collection_of_coins],
    'immutable': [lucky_number, pi, one_is_a_prime_number, name, profile_info, ]
}
# def sort_args_type(**kwargs) -> dict[list]:
#     # sorted_variables = {'mutable': [], 'immutable': []}
#
#     # Cycle for checking each arg type and putting to one of two lists
#     for variable, value in kwargs:
#         if (
#                 str(type(value).__name__) == "int"
#                 or str(type(value).__name__) == "float"
#                 or str(type(value).__name__) == "tuple"
#                 or str(type(value).__name__) == "bool"
#                 or str(type(value).__name__) == "NoneType"
#         ):
#             sorted_variables['mutable'].append(value)
#         elif (
#                 str(type(value).__name__) == "list"
#                 or str(type(value).__name__) == "dict"
#                 or str(type(value).__name__) == "set"
#         ):
#             sorted_variables['immutable'].append(value)
#
#     return sorted_variables