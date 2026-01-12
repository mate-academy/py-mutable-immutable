lucky_number = 777 # int
pi = 3.14 # float
one_is_a_prime_number = False # bool
name = "Richard" # str
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
] # list
profile_info = ("michel", "michel@gmail.com", "12345678") # tuple
marks = {
    "John": 4,
    "Sergio": 3,
} # dict
collection_of_coins = {1, 2, 25} # set


mutable_list = []
immutable_list = []



sorted_variables = {
"mutable": [my_favourite_films, marks, collection_of_coins],
"immutable": [profile_info, lucky_number, pi, one_is_a_prime_number, name]
}

print(sorted_variables)