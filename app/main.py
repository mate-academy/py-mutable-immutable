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

# mutable: list (my_favourite_films), dict (marks), set (collection...)
# immutable: int (lucky_number), float (pi), bool (one_is_a_prime_number), str (name), tuple (profile info)


# Sorting variables into "mutable" and "immutable"
sorted_variables = {
    "mutable": [],
    "immutable": []
}

# Check each variable and categorize it
for var in [lucky_number, pi, one_is_a_prime_number, name, my_favourite_films, profile_info, marks, collection_of_coins]:
    if isinstance(var, (list, dict, set)):  # Mutable types
        sorted_variables["mutable"].append(var)
    else:  # Immutable types
        sorted_variables["immutable"].append(var)

# Print the result
print(sorted_variables)
