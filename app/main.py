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


def sort_variables(list_object: list) -> dict:
    my_sorted_variables = {"mutable": [], "immutable": []}
    for variable_object in list_object:
        if isinstance(variable_object, (int, str, bool, float, tuple)):
            my_sorted_variables["immutable"].append(variable_object)
        else:
            my_sorted_variables["mutable"].append(variable_object)
    return my_sorted_variables


my_object = [lucky_number, pi, one_is_a_prime_number, name,
             my_favourite_films, profile_info, marks, collection_of_coins]
sorted_variables = sort_variables(my_object)
