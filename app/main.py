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


def sorted_variables(*args) -> dict:
    sort_variables = {}
    mutable_ls = []
    immutable_ls = []

    for item in args:
        if isinstance(item, (list, dict, set)):
            mutable_ls.append(item)
        else:
            immutable_ls.append(item)
    sort_variables["mutable"] = mutable_ls
    sort_variables["immutable"] = immutable_ls

    return sort_variables
