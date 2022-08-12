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

sorted_variable = {
    "mutable": [],
    "immutable": [],
}


def determine_type_variable(var) -> dict:

    if type(var) in [set, dict, list]:
        sorted_variable["mutable"].append(var)
    else:
        sorted_variable["immutable"].append(var)

    return sorted_variable
