# int (immutable)
lucky_number = 777
# float (immutable)
pi = 3.14
# bool (immutable)
one_is_a_prime_number = False
# str (immutable)
name = "Richard"
# list (mutable)
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
# tuple (immutable)
profile_info = ("michel", "michel@gmail.com", "12345678")
# dict (mutable)
marks = {
    "John": 4,
    "Sergio": 3,
}
# set (mutable)
collection_of_coins = {1, 2, 25}

sorted_variables = {
    "mutable": [],
    "immutable": []
}


def sort_list(variables: list) -> None:
    for collections in variables:
        if isinstance(collections, (list, dict, set)):
            sorted_variables["mutable"].append(collections)
        elif isinstance(collections, (int, float, str, tuple, bool)):
            sorted_variables["immutable"].append(collections)


variables_full = [
    lucky_number,
    pi, one_is_a_prime_number,
    name, my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
]

print(sort_list(variables_full))
