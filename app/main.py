# Дані змінні
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

def classify_variables(*args) -> dict:
    mutable_types = (list, set, dict)
    immutable_types = (int, float, str, bool, type(None), tuple)

    result = {
        "mutable": [],
        "immutable": []
    }

    for arg in args:
        if isinstance(arg, mutable_types):
            result["mutable"].append(arg)
        elif isinstance(arg, immutable_types):
            result["immutable"].append(arg)

    return result

sorted_variables = classify_variables(
    lucky_number, pi, one_is_a_prime_number, name, my_favourite_films,
    profile_info, marks, collection_of_coins
)
