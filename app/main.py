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


def print_variable(valor: any) -> str:
    for name, valor_name in globals().items():
        if valor_name == valor and not name.startswith("__"):
            return name
    return None


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
            mutable_immutable["immutable"].append(print_variable(arg))
        else:
            mutable_immutable["mutable"].append(print_variable(arg))

    return mutable_immutable


variables_types(
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
)
