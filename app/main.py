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

# Initialize dictionary to store mutable and immutable variables
sorted_variables = {"mutable": [],
                    "immutable": []}


def sort_variables(*args) -> dict:
    # Define mutable types
    mutable_types = (list, dict, set)
    # Sort variables as mutable or immutable
    for element in args:
        if isinstance(element, mutable_types):
            sorted_variables["mutable"].append(element)
        else:
            sorted_variables["immutable"].append(element)
    return sorted_variables


sort_variables(lucky_number, pi, one_is_a_prime_number, name,
               my_favourite_films, profile_info, marks, collection_of_coins)
