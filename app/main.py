# mutable variable - list, dictionary, set
# immutable variable - int, float, bool, string, tuple

# int
lucky_number = 777

# float
pi = 3.14

# bool
one_is_a_prime_number = False

# string
name = "Richard"

# list
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]

# tuple
profile_info = ("michel", "michel@gmail.com", "12345678")

# dictionary
marks = {
    "John": 4,
    "Sergio": 3,
}

# set
collection_of_coins = {1, 2, 25}

variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]
mutable = []
immutable = []

mutable_types = (list, dict, set)

mutable = [var for var in variables if isinstance(var, mutable_types)]
immutable = [var for var in variables if not isinstance(var, mutable_types)]

sorted_variables = {"mutable": mutable, "immutable": immutable}
