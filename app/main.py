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


sorted_variables = {
    "mutable": [],
    "immutable": []
}


obj = {
    "lucky_number": 777,
    "pi": 3.14,
    "one_is_a_prime_number": False,
    "name": "Richard",
    "my_favourite_films": [
        "The Shawshank Redemption",
        "The Lord of the Rings: The Return of the King",
        "Pulp Fiction",
        "The Good, the Bad and the Ugly",
        "The Matrix",
    ],
    "profile_info": ("michel", "michel@gmail.com", "12345678"),
    "marks": {"John": 4, "Sergio": 3},
    "collection_of_coins": {1, 2, 25},
}


def sort_obj(obj: any) -> any:
    if isinstance(obj, (list, set, dict)):
        sorted_variables["mutable"].append(obj)
    else:
        sorted_variables["immutable"].append(obj)

    return print(sorted_variables)


for key, value in obj.items():
    if key in ["sort_variables", "sorted_variables"] or name.startswith("__"):
        continue
    sort_obj(value)
