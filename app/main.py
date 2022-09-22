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

def sort_vareibles(*args):
    sorted_variables = {"mutable": [], "immutable": []}
    if type(args) == str or type(args) == int or type(args) == float or type(args) == tuple or type(args) == bool:
        sorted_variables["immutable"].append(args)
    else:
        sorted_variables["mutable"].append(args)
    return sorted_variables
