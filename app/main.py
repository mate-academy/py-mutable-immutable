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

# Separate mutable and immutable variables
mutable_variables = [my_favourite_films, marks, collection_of_coins]
immutable_variables = [lucky_number, pi, one_is_a_prime_number,
                       name, profile_info]

# Create the sorted_variables dictionary
sorted_variables = {
    "mutable": mutable_variables,
    "immutable": immutable_variables
}

# Print the result
print(sorted_variables)
