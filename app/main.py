from typing import MutableSet, MutableSequence, MutableMapping

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

# List of variables to check if mutable or immutable
variable_list = [lucky_number, pi, one_is_a_prime_number, name,
                 my_favourite_films, profile_info, marks, collection_of_coins]


def is_mutable(variable_to_check: any) -> bool:
    """
    Determines if a given variable is mutable.

    An object is considered mutable if it belongs to the mutable
    collection types: set, list, dict, or their subclasses.

    :param variable_to_check: The variable to check
        if its mutable or immutable.
    :type variable_to_check: Any
    :return: ``True`` if the variable is mutable, or ``False`` if immutable.
    :rtype: bool
    """
    return isinstance(variable_to_check,
                      (MutableSet, MutableSequence, MutableMapping))


def sort_variables_by_mutability(variables_to_check: list[any]) \
        -> dict[str, list[any]]:
    """
    Sort a list of variables into mutable and immutable categories.

    This function classifies each variable in the given list as either
    mutable or immutable.

    :param variables_to_check: A list of variables to be classified.
    :type variables_to_check: list[Any]
    :return: A dictionary with two keys:
        ``"mutable"``: A list of mutable variables.
        ``"immutable"``: A list of immutable variables.
    :rtype: dict[str, list[Any]]
    """

    result = {"mutable": [],
              "immutable": []}

    for variable_to_check in variables_to_check:
        if is_mutable(variable_to_check):
            result["mutable"].append(variable_to_check)
        else:
            result["immutable"].append(variable_to_check)
    return result


sorted_variables = sort_variables_by_mutability(variable_list)
