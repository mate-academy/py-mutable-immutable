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

# Function that checks if lucky_number is mutable or immutable
if id(lucky_number) == id(lucky_number + 1):
    sorted_variables["mutable"].append(lucky_number)
else:
    sorted_variables["immutable"].append(lucky_number)

# Function that checks if pi is mutable or immutable
if id(pi) == id(pi + 1):
    sorted_variables["mutable"].append(pi)
else:
    sorted_variables["immutable"].append(pi)

# Function that checks if one_is_a_prime_number is mutable or immutable
if id(one_is_a_prime_number) == id(one_is_a_prime_number + True):
    sorted_variables["mutable"].append(one_is_a_prime_number)
else:
    sorted_variables["immutable"].append(one_is_a_prime_number)

# Function that checks if name is mutable or immutable
if id(name) == id(name + "s"):
    sorted_variables["mutable"].append(name)
else:
    sorted_variables["immutable"].append(name)

# Function that checks if my_favourite_films is mutable or immutable
update_my_favourite_films = my_favourite_films
if id(my_favourite_films) != id(update_my_favourite_films + ["2012"]):
    sorted_variables["mutable"].append(my_favourite_films)
else:
    sorted_variables["immutable"].append(my_favourite_films)

# Function that checks if profile_info is mutable or immutable
if profile_info == profile_info + (4,):
    sorted_variables["mutable"].append(profile_info)
else:
    sorted_variables["immutable"].append(profile_info)

# Function that checks if marks is mutable or immutable
if marks == dict(marks):
    sorted_variables["mutable"].append(marks)
else:
    sorted_variables["immutable"].append(marks)

# Function that checks if collection_of_coins is mutable or immutable
if collection_of_coins == set(collection_of_coins):
    sorted_variables["mutable"].append(collection_of_coins)
else:
    sorted_variables["immutable"].append(collection_of_coins)
