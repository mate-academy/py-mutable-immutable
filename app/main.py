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

variable_names = [
    "lucky_number",
    "pi",
    "one_is_a_prime_number",
    "name",
    "my_favourite_films",
    "profile_info",
    "marks",
    "collection_of_coins"
]

# get values by names
variable_values = [globals()[name] for name in variable_names]

# lists with corresponding types
mutable = [list, dict, set]
immutable = [int, float, str, bool, tuple]

sorted_variables = {
    "mutable": [],
    "immutable": []
}

# assign values to dict
for variable_value in variable_values:
    if type(variable_value) in mutable:
        sorted_variables["mutable"].append(variable_value)
    else:
        sorted_variables["immutable"].append(variable_value)
