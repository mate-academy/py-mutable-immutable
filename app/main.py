from typing import Union

lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favorite_films = [
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


variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favorite_films,
    profile_info,
    marks,
    collection_of_coins
]

sorted_variables = {
    "mutable": [],
    "immutable": []
}


def categorize_variables(item: Union[list, dict, set]) -> None:
    if isinstance(item, (list, set, dict)):
        sorted_variables["mutable"].append(item)
    else:
        sorted_variables["immutable"].append(item)


for item in variables:
    categorize_variables(item)

print(sorted_variables)
