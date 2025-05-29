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
immutable_types = (int, float, str, tuple)

sorted_variables = {
    "mutable": [var for var in [lucky_number, marks,
                                one_is_a_prime_number, name,
                                my_favourite_films, profile_info,
                                collection_of_coins,
                                pi] if isinstance(var, mutable_types)],
    "immutable": [var for var in [lucky_number, collection_of_coins,
                                  one_is_a_prime_number, name,
                                  my_favourite_films, profile_info,
                                  marks,
                                  pi] if isinstance(var, immutable_types)],
}
