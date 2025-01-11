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

sorted_variables = {}


def sorted_dict(*args: object) -> object:
    mutable_list = []
    immutable_list = []
    for arg in args:
        if isinstance(arg, (list, set, dict)):
            mutable_list.append(arg)
        else:
            immutable_list.append(arg)
    sorted_variables["mutable"] = mutable_list
    sorted_variables["immutable"] = immutable_list

    return sorted_variables


sorted_dict(lucky_number, pi, one_is_a_prime_number, name, my_favourite_films,
            profile_info, marks, collection_of_coins)
