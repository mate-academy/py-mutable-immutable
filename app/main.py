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

def types_variables(variables):
    sorted_variables = {
        "mutable": [],
        "immutable": []
    }

    for variable in variables:
        if isinstance(variable, tuple):
            if all(not isinstance(el, list) for el in variable):
                sorted_variables["immutable"].append(variable)
            else:
                sorted_variables["mutable"].append(variable)
        elif isinstance(variable, list):
            sorted_variables["mutable"].append(variable)

    return sorted_variables
