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

    for var_name in [_ for _ in args[0] if not _.startswith("_")]:
        if (type(eval(var_name)) is dict or type(eval(var_name)) is list
                or type(eval(var_name)) is set):
            result["mutable"].append(eval(var_name))
            continue
        result["immutable"].append(eval(var_name))

    return result


sorted_variables = _variable_sorter(dir())
