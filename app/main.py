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

variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
]
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
for variable_name, variable_value in zip(variable_names, variables):
    print(f"{variable_name}: {type(variable_value)}")

mutable_types = (list, dict, set, bytearray)
immutable_types = (int, float, str, tuple, bool, frozenset, bytes)

sorted_variables = {"mutable": [], "immutable": []}
for variable_value in variables:
    if isinstance(variable_value, mutable_types):
        sorted_variables["mutable"].append(variable_value)
    elif isinstance(variable_value, immutable_types):
        sorted_variables["immutable"].append(variable_value)

print("\nSorted variables:")
print(sorted_variables)
