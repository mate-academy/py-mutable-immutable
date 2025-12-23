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


def is_immutable(obj: Any) -> bool:
    return isinstance(obj, (int, float, bool, str, tuple))


# Sorting the variables
sorted_variables = {
    "mutable": [],
    "immutable": []
}

variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins]

for my_variable in variables:
    if is_immutable(my_variable):
        sorted_variables["immutable"].append(my_variable)
    else:
        sorted_variables["mutable"].append(my_variable)
