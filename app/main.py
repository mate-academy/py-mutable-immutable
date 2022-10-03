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


def make_dict(*args):
    mutable_immutable_dict = {
        "mutable": [],
        "immutable": []
    }

    for arg in args:
        if (
                isinstance(arg, str)
                or isinstance(arg, int)
                or isinstance(arg, float)
                or isinstance(arg, tuple)
                or isinstance(arg, bool)
        ):
            mutable_immutable_dict["immutable"].append(arg)
        else:
            mutable_immutable_dict["mutable"].append(arg)

    return mutable_immutable_dict


sorted_variables = make_dict(
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
)
