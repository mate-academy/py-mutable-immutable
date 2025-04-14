lucky_number = 777  # int -> immutable
pi = 3.14   #float ->  immutable
one_is_a_prime_number = False #bool -> immutable
name = "Richard"    #str -> immutable
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]   # -> list mutable
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
} # dict -> mutable
collection_of_coins = {1, 2, 25}    # set -> mutable

sorted_variables = {
    "mutable": [my_favourite_films, marks, collection_of_coins],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info],
}
