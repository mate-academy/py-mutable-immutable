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
sorted_variables = {'mutable': [], 'immutable': []}

from typing import Any
def sort_category(*args):
    sorted_vars = {
        'mutable': sorted_variables['mutable'][:],
        'immutable': sorted_variables['immutable'][:]
    }
    for arg in args:
        if isinstance(arg, (list, dict, set)):
            sorted_vars['mutable'].append(arg)
        else:
            sorted_vars['immutable'].append(arg)
    return sorted_vars

sorted_variables = sort_category(lucky_number, pi, one_is_a_prime_number, name, my_favourite_films, profile_info, marks, collection_of_coins)


