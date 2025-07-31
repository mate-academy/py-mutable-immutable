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

mutable_types = (list, dict, set)
immutable_types = (int, float, str, tuple, bool)

mutables = []
immutables = []

for var_name, value in list(globals().items()):
    if isinstance(value, mutable_types):
        mutables.append(value)
    elif isinstance(value, immutable_types):
        immutables.append(value)

sorted_variables = {
    "mutable": mutables,
    "immutable": immutables
}
