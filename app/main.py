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


def sort_type(**kwargs) -> dict:
    result = {}
    for key, i in kwargs.items():
        if not isinstance(i, (list, dict, set)):
            if "immutable" not in result:
                result["immutable"] = [key]
            else:
                result["immutable"].append(key)
        else:
            if "mutable" not in result:
                result["mutable"] = [key]
            else:
                result["mutable"].append(key)
    return result


print(sort_type(lucky_number=777,
                pi=3.14,
                one_is_a_prime_number=False,
                name="Richard",
                my_favourite_films=[
                    "The Shawshank Redemption",
                    "The Lord of the Rings: The Return of the King",
                    "Pulp Fiction",
                    "The Good, the Bad and the Ugly",
                    "The Matrix", ],
                profile_info=("michel", "michel@gmail.com", "12345678"),
                marks={"John": 4, "Sergio": 3, },
                collection_of_coins={1, 2, 25}))
