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

all_variables_array = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]


def is_mutable(obj: Any) -> bool:
    """
    Return True if obj is mutable else - return False.
    """
    return isinstance(obj, (list, dict, set))


sorted_variables = {"mutable": [], "immutable": []}


for current_value in all_variables_array:
    key = "mutable" if is_mutable(current_value) else "immutable"
    sorted_variables[key].append(current_value)
