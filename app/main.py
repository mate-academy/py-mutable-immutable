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

sorted_variables = {
    "mutable": [],
    "immutable": []
}

variables = {
    "lucky_number": lucky_number,
    "pi": pi,
    "one_is_a_prime_number": one_is_a_prime_number,
    "name": name,
    "profile_info": profile_info,
    "my_favourite_films": my_favourite_films,
    "marks": marks,
    "collection_of_coins": collection_of_coins,
}

mutable_types = (list, dict, set)

for var_name, var_value in variables.items():
    if isinstance(var_value, mutable_types):
        sorted_variables["mutable"].append(var_value)
    else:
        sorted_variables["immutable"].append(var_value)

print("Sorted Variables Dictionary:")
print("Mutable Variables:")
for var in sorted_variables["mutable"]:
    print(var)

print("\nImmutable Variables:")
for var in sorted_variables["immutable"]:
    print(var)