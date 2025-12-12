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


def mutable_or_inmutable(*args) -> dict:

    mutable = []
    immutable = []
    mutable_colection = {set, list, dict}
    immutable_colection = {int, float, bool, str, tuple}

    for arg in args:
        if type(arg) in mutable_colection:
            mutable.append(arg)
        elif type(arg) in immutable_colection:
            immutable.append(arg)
    return {"mutable": mutable, "immutable": immutable}


sorted_variables = mutable_or_inmutable(
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
)
