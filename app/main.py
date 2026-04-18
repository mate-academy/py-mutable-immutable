from typing import Any
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

# write your code here

IMMUTABLE_TYPES = (int, float, str, tuple, bool, bytes, frozenset)
MUTABLE_TYPES = (list, dict, set, bytearray)

sorted_variables = {
    "mutable" : [],
    "immutable" : []
}


def check_mutability(obj : Any, sorted_dict : dict) :
    if isinstance(obj, IMMUTABLE_TYPES):
        sorted_dict["immutable"].append(obj)
    elif isinstance(obj, MUTABLE_TYPES):
        sorted_dict["mutable"].append(obj)


all_test_variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
]

for test_variable in all_test_variables:
    check_mutability(test_variable, sorted_variables)

print(sorted_variables)
