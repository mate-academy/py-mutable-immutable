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

variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]


def check_mutability(variables: list) -> dict:
    sorted_variables = {
        "mutable": [],
        "immutable": [],
    }
    for declared_variable in variables:
        if type(declared_variable) in (list, dict, set):
            sorted_variables["mutable"].append(declared_variable)
        else:
            sorted_variables["immutable"].append(declared_variable)
    return sorted_variables


sorted_variables = check_mutability(variables)
