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


def create_sorted_variables() -> dict[str, list]:
    sort_variables = {
        "mutable": [],
        "immutable": []
    }

    variables = [
        lucky_number,
        pi,
        one_is_a_prime_number,
        name,
        my_favourite_films,
        profile_info,
        marks,
        collection_of_coins
    ]

    for current in variables:
        if isinstance(current, (list, dict, set)):
            sort_variables["mutable"].append(current)
        elif isinstance(current, (int, float, str, bool, tuple, type(None))):
            sort_variables["immutable"].append(current)
        else:
            print(f"Cannot classify {current} into 'mutable' or 'immutable'")

    return sort_variables


sorted_variables = create_sorted_variables()
