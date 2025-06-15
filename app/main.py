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

# Store all variables in a list
variables = []

# Mutable and immutable types
mutable_types = (list, dict, set)
immutable_types = (int, str, float, tuple, frozenset)

# Classify using isinstance
sorted_variables = {
    "mutable": [var for var in variables if isinstance(var, mutable_types)],
    "immutable": [var for var in variables if isinstance(var, immutable_types)]
}

print(sorted_variables)
