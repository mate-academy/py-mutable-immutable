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


def sort_varibles(*args) -> dict:
    sorted_variables = {}
    mutable_types = (list, dict, set)

    for variable_to_check in args:
        if type(variable_to_check) in mutable_types:
            if "mutable" not in sorted_variables:
                sorted_variables["mutable"] = [variable_to_check]
            else:
                sorted_variables["mutable"].append(variable_to_check)
        else:
            if "immutable" not in sorted_variables:
                sorted_variables["immutable"] = [variable_to_check]
            else:
                sorted_variables["immutable"].append(variable_to_check)

    return sorted_variables


sorted_variables = sort_varibles(
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
)

print(sorted_variables)
