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

# Updated profile_info to be a tuple
profile_info = ("michel", "michel@gmail.com", "12345678")

marks = {"John": 4, "Sergio": 3}
collection_of_coins = {1, 2, 25}

# Categorize variables into 'mutable' and 'immutable'
sorted_variables = {
    "mutable": [
        my_favourite_films,
        profile_info,  # This should now be a tuple
        marks,
        collection_of_coins
    ],
    "immutable": [
        lucky_number,
        pi,
        one_is_a_prime_number,
        name
    ]
}
