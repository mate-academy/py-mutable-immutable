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

variables = [lucky_number, pi, one_is_a_prime_number, name,
             my_favourite_films, profile_info, marks, collection_of_coins]
sorted_variables = {
    "mutable": [],
    "immutable": []
}


def is_mutable(obj: object) -> bool:
    mutable_types = (list, dict, set)

    return isinstance(obj, mutable_types)


def is_immutable(obj: object) -> bool:
    immutable_types = (int, float, str, bool, tuple, type(None))

    return isinstance(obj, immutable_types)


for objects in variables:
    if is_mutable(objects):
        sorted_variables["mutable"].append(objects)
    else:
        sorted_variables["immutable"].append(objects)
