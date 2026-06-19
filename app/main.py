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

# Create a dictionary categorized by data types
sorted_variables = {
    "mutable": [
        my_favourite_films,  # List []
        marks,  # Dictionary {}
        collection_of_coins,  # Set {}, with single values
    ],
    "immutable": [
        lucky_number,  # Integer (int)
        one_is_a_prime_number,  # Boolean value (bool)
        pi,  # Floating-point number (float)
        name,  # String (str)
        profile_info,  # Tuple ()
    ]
}
