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


def sort_variables(variables: list) -> dict:
    immutable = [int, float, str, bool, tuple]
    sort_dict = {
        "mutable": [],
        "immutable": []
    }

    for one_variable in variables:
        if type(one_variable) in immutable:
            sort_dict["immutable"].append(one_variable)
        else:
            sort_dict["mutable"].append(one_variable)

    return sort_dict


sorted_variables = sort_variables(
    [lucky_number, pi, one_is_a_prime_number, name,
     my_favourite_films, profile_info, marks, collection_of_coins
     ])
