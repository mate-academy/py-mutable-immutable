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

# Values of change as mutable or immutable
mutable_types = (list, dict, set)
immutable_types = (int, float, str, tuple, bool)

# Dictionary creation sorted_variables
sorted_variables = {
    "mutable": [],
    "immutable": []
}

# Adding special to special lists
variables = [
    lucky_number, pi, one_is_a_prime_number, name,
    my_favourite_films, profile_info, marks, collection_of_coins
]

for var in variables:
    if isinstance(var, mutable_types):
        sorted_variables["mutable"].append(var)
    elif isinstance(var, immutable_types):
        sorted_variables["immutable"].append(var)

# result
print(sorted_variables)


