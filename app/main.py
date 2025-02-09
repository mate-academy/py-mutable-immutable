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


def sorted_variable(variable_mutable_immutable: str) -> dict:

    if isinstance(variable_mutable_immutable, (int, str, bool, float, tuple)):
        sorted_variables["immutable"].append(variable_mutable_immutable)
    else:
        sorted_variables["mutable"].append(variable_mutable_immutable)


sorted_variable(lucky_number)
sorted_variable(pi)
sorted_variable(one_is_a_prime_number)
sorted_variable(name)
sorted_variable(my_favourite_films)
sorted_variable(profile_info)
sorted_variable(marks)
sorted_variable(collection_of_coins)
