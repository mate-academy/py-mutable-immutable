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

# Create an empty dictionary to store the sorted variables
sorted_variables = {"mutable": [], "immutable": []}

# Categorize the variables based on mutability
vars = [lucky_number, pi, one_is_a_prime_number, name, my_favourite_films, profile_info, marks, collection_of_coins]
mutable = [list, dict, set]

for item in vars:
    if type(item) in mutable:
        sorted_variables["mutable"].append(item)
    else:
        sorted_variables["immutable"].append(item)
