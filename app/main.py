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


def sort_variable(*args) -> dict:
    return_dict = {"mutable": [], "immutable": []}
    for obj in args:
        if isinstance(obj, (list, dict, set)):
            return_dict["mutable"].append(obj)
        else:
            return_dict["immutable"].append(obj)
    return return_dict


sorted_variables = sort_variable(lucky_number, pi, one_is_a_prime_number,
                                 name, my_favourite_films, profile_info,
                                 marks, collection_of_coins)
