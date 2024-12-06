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

"""
Identify the type of each variable and store them in a dictionary with the
following structure:
{
    "mutable": [list, set, dict],
    "immutable": [int, float, complex, str, tuple]
}
"""
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
immutables = (int, float, complex, str, tuple, frozenset, bytes)
sorted_variables = {"mutable": [], "immutable": []}

for variable_name in variable_names:
    local_vars = locals()
    value = local_vars.get(variable_name)
    if (isinstance(value, immutables)):
        sorted_variables["immutable"].append(value)
    else:
        sorted_variables["mutable"].append(value)

print(f"{sorted_variables}")
