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

variable_mass = \
    [
        lucky_number,
        pi,
        one_is_a_prime_number,
        name,
        my_favourite_films,
        profile_info,
        marks,
        collection_of_coins,
    ]


def sorted_variables(mass: list) -> dict:
    result = {
        "mutable": [],
        "immutable": [],
    }

    for arg in mass:
        if isinstance(arg, (list, set, dict)):
            result["mutable"].append(arg)
        if isinstance(arg, (int, float, bool, str, tuple)):
            result["immutable"].append(arg)

    return result


sorted_variables = sorted_variables(variable_mass)
