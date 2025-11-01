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


def to_sort_variables(*args) -> dict:
    result_dict = {
        "mutable": [],
        "immutable": []
    }
    for item in args:
        if type(item) == dict or type(item) == list or type(item) == set:
            result_dict["mutable"].append(item)
        else:
            result_dict["immutable"].append(item)
    return result_dict
