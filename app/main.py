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
    "Sergio": (3),
}
collection_of_coins = {1, 2, 25}


def variables_types(*args: any) -> dict:
    mutable_immutable = {
        "mutable": [],
        "immutable": [],
    }

    for arg in args:
        if isinstance(arg, (int,
                            float,
                            str,
                            bool,
                            type(None),
                            tuple)) or callable(arg):
            mutable_immutable["immutable"].append(arg)
        else:
            mutable_immutable["mutable"].append(arg)

    return mutable_immutable


sorted_variables = variables_types(
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
)

print(sorted_variables)
