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
    mutable_types = [list, dict, set]
    immutable_types = [tuple, str, int, float, bool]
    mutable = []
    immutable = []
    for arg in args:
        if type(arg) in mutable_types:
            mutable.append(arg)
        if type(arg) in immutable_types:
            immutable.append(arg)
    return {"mutable": mutable, "immutable": immutable}


sorted_variables = sort_variables(lucky_number, pi, one_is_a_prime_number, name, my_favourite_films, profile_info, marks, collection_of_coins)
