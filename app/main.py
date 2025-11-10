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

def sorted_variables(*args):
    d = {}
    for index, arg in enumerate(args):
        if isinstance(arg, (int, float, str, bool, tuple, type(None))) or callable(arg):
            d[arg] = index
        else:
            print(f"Cannot add {arg} to the dict!")
    return d
print(sorted_variables(lucky_number,pi,one_is_a_prime_number,name,my_favourite_films))