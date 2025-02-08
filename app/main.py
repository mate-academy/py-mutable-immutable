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



def sorted_variables(variable) -> dict:
    sorted_variable = {"mutable": [],
                       "immutable": []
                       }
    for var in variable:

        for name, value in globals().items():
            if value is var:
                variable_name = name

        if isinstance(var, (int, str, bool, float, tuple)):
            sorted_variable["immutable"].append(str(variable_name))
        else:
            sorted_variable["mutable"].append(str(variable_name))

    return sorted_variable

