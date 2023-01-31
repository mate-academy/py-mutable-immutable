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
sorted_variables = {"mutable": [], "immutable": []}
mutable = set, dict, list
immutable = int, float, str, tuple, bool
if type(lucky_number) in mutable:
    sorted_variables["mutable"].append(lucky_number)
else:
    sorted_variables["immutable"].append(lucky_number)
if type(pi) in mutable:
    sorted_variables["mutable"].append(pi)
else:
    sorted_variables["immutable"].append(pi)
if type(one_is_a_prime_number) in mutable:
    sorted_variables["mutable"].append(one_is_a_prime_number)
else:
    sorted_variables["immutable"].append(one_is_a_prime_number)
if type(name) in mutable:
    sorted_variables["mutable"].append(name)
else:
    sorted_variables["immutable"].append(name)
if type(my_favourite_films) in mutable:
    sorted_variables["mutable"].append(my_favourite_films)
else:
    sorted_variables["immutable"].append(my_favourite_films)
if type(profile_info) in mutable:
    sorted_variables["mutable"].append(profile_info)
else:
    sorted_variables["immutable"].append(profile_info)
if type(marks) in mutable:
    sorted_variables["mutable"].append(marks)
else:
    sorted_variables["immutable"].append(marks)
if type(collection_of_coins) in mutable:
    sorted_variables["mutable"].append(collection_of_coins)
else:
    sorted_variables["immutable"].append(collection_of_coins)
print(sorted_variables)
