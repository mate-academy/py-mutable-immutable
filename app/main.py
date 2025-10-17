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

def sorted_variables(variables) -> dict:
    '''
    Sorted variables to mutable and immutable.

    :param variables: any
    :return: dictionary
    '''
    immutable_types = (int, str, bool, float, tuple)
    sorted_variable_result = {"immutable": [], "mutable": []}

    if variables is None:
        return sorted_variable_result
    for variable in variables:
        if isinstance(variables, immutable_types):
            sorted_variable_result["immutable"].append(variable)
        else:
            sorted_variable_result["mutable"].append(variable)
    return sorted_variable_result
