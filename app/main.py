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


def _variable_sorter(*args) -> dict:

    result = {"mutable": [], "immutable": [], }

    for var_name in args:
        if (isinstance(var_name, set) or isinstance(var_name, dict)
                or isinstance(var_name, list)):
            result["mutable"].append(var_name)
            continue
        result["immutable"].append(var_name)

    return result


sorted_variables = _variable_sorter(
    lucky_number, pi, one_is_a_prime_number, marks,
    name, my_favourite_films, profile_info, collection_of_coins
)
