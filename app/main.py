lucky_number = 777 # immutable
pi = 3.14 # immutable
one_is_a_prime_number = False # immutable
name = "Richard" # immutable
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
] #mutavel
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

mutable = [my_favourite_films, marks, collection_of_coins]
immutable = [
        lucky_number, pi, one_is_a_prime_number, name,
        profile_info
    ]

sorted_variables = {
    "mutable": mutable,
    "immutable": immutable
}
