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
    results = {}
    mutable = []
    immutable = []

    for argument in args:
        if callable(argument) or isinstance(argument, (list, set, dict)) or (
                isinstance(argument, tuple)
                and any(isinstance(i, (list, set, dict)) for i in argument)
        ):
            mutable.append(argument)
        else:
            immutable.append(argument)

    results["mutable"] = mutable
    results["immutable"] = immutable
    return results


sorted_variables = sort_variables(lucky_number, pi, one_is_a_prime_number,
                                  name, my_favourite_films, profile_info,
                                  marks, collection_of_coins)
