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




def sort_variables(variable, values):

    sorted_variables = {"mutable": [], "immutable": []}

    for values in variable:
        for var in values:
        # variable_type = type(variable_name)._name_
        # if variable_type in [list, dict, set]:
        #     sorted_variables["mutable"].append(variable_name)
        # else:
        #     sorted_variables["immutable"].append(variable_name)
            if isinstance(var, (list, dict, set)):
                sorted_variables["mutable"].append(variable_name)
            elif isinstance(var, (int, float, bool, str, tuple)):
                sorted_variables["immutable"].append(variable_name)
    return sorted_variables
