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

    mutable = []
    imutable = []
    for arg in args:
        if isinstance(arg, (list, set, dict)):
            mutable.append(arg)
        else:
            imutable.append(arg)

    return {
        "mutable": mutable,
        "imutable": imutable
    }
