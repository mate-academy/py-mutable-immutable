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

list_name = [lucky_number, pi, one_is_a_prime_number, name, my_favourite_films,
             profile_info, marks, collection_of_coins]


def sorted_var(name_of_variable: list) -> dict:
    sorted_v = {
        "mutable": [],
        "immutable": []
    }
    element_list = [list, set, dict]
    for var_name in name_of_variable:
        if type(var_name) in element_list:
            sorted_v["mutable"] += [var_name]
        else:
            sorted_v["immutable"] += [var_name]

    return sorted_v


sorted_variables = sorted_var(list_name)
