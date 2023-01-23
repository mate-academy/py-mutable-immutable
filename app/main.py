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

types_to_sort = [lucky_number, pi, one_is_a_prime_number,
                 name, my_favourite_films, profile_info,
                 marks, collection_of_coins]

sorted_variables = {"mutable": [], "immutable": []}

for current_type in types_to_sort:
    if type(current_type) == bool or type(current_type) == int or \
            type(current_type) == float or type(current_type) == tuple or \
            type(current_type) == str or type(current_type) == frozenset:
        sorted_variables["immutable"].append(current_type)
    else:
        sorted_variables["mutable"].append(current_type)
