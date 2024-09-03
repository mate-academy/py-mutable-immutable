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


def sort_variables_by_mutability(*args) -> dict[str, list]:
    """Sort variables by their mutability.

    Args:
        *args: A list of variables.

    Returns:
        dict: A dictionary with two keys: "mutable" and "immutable".
        Each value is a list containing variables of the corresponding type.
    """
    sorted_variables = {
        "mutable": [],
        "immutable": [],
    }

    for element in args:
        if isinstance(element, (list, dict, set)):
            sorted_variables["mutable"].append(element)
        else:
            sorted_variables["immutable"].append(element)

    return sorted_variables


sorted_variables = sort_variables_by_mutability(
    lucky_number, pi, one_is_a_prime_number,
    name, my_favourite_films, profile_info,
    marks, collection_of_coins,
)
