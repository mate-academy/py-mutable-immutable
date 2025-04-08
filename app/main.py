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
    sorted_variables = {
        "mutable": [],
        "immutable": []
    }

    mutable_types = (list, dict, set, bytearray)
    immutable_types = (int, float, str, tuple, bool, bytes)

    for arg in args:
        if isinstance(arg, mutable_types):
            sorted_variables["mutable"].append(arg)
        elif isinstance(arg, immutable_types):
            sorted_variables["immutable"].append(arg)
        else:
            pass

    return sorted_variables


sorted_variables = sort_variables(
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
)
