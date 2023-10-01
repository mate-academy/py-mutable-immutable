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


def sort_variables(*args) -> dict:
    sorted_variables = {"mutable": [], "immutable": []}

    for arg in args:
        if isinstance(arg, list):
            sorted_variables["mutable"].append("my_favourite_films")
        elif isinstance(arg, dict):
            sorted_variables["mutable"].append("marks")
        elif isinstance(arg, set):
            sorted_variables["mutable"].append("profile_info")
        elif isinstance(arg, int):
            sorted_variables["immutable"].append("lucky_number")
        elif isinstance(arg, bool):
            sorted_variables["immutable"].append("one_is_a_prime_number")
        elif isinstance(arg, float):
            sorted_variables["immutable"].append("pi")
        else:
            sorted_variables["immutable"].append("name")

    return sorted_variables
