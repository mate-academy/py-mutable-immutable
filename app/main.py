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
    "mutable": [],
    "immutable": []
}


def add_to_sorted(value: object) -> None:

    mutable_types = (dict, list, set)
    if isinstance(value, mutable_types):
        sorted_variables["mutable"].append(value)
    else:
        sorted_variables["immutable"].append(value)


add_to_sorted(lucky_number)
add_to_sorted(pi)
add_to_sorted(one_is_a_prime_number)
add_to_sorted(name)
add_to_sorted(my_favourite_films)
add_to_sorted(profile_info)
add_to_sorted(marks)
add_to_sorted(collection_of_coins)
