def is_immutable(obj: any) -> bool:
    if isinstance(obj, (int, str, bool, float, tuple)):
        return True
    return False


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

if is_immutable(lucky_number):
    sorted_variables["immutable"].append(lucky_number)
else:
    sorted_variables["mutable"].append(lucky_number)

if is_immutable(pi):
    sorted_variables["immutable"].append(pi)
else:
    sorted_variables["mutable"].append(pi)

if is_immutable(one_is_a_prime_number):
    sorted_variables["immutable"].append(one_is_a_prime_number)
else:
    sorted_variables["mutable"].append(one_is_a_prime_number)

if is_immutable(name):
    sorted_variables["immutable"].append(name)
else:
    sorted_variables["mutable"].append(name)

if is_immutable(my_favourite_films):
    sorted_variables["immutable"].append(my_favourite_films)
else:
    sorted_variables["mutable"].append(my_favourite_films)

if is_immutable(profile_info):
    sorted_variables["immutable"].append(profile_info)
else:
    sorted_variables["mutable"].append(profile_info)

if is_immutable(marks):
    sorted_variables["immutable"].append(marks)
else:
    sorted_variables["mutable"].append(marks)

if is_immutable(collection_of_coins):
    sorted_variables["immutable"].append(collection_of_coins)
else:
    sorted_variables["mutable"].append(collection_of_coins)

if is_immutable(sorted_variables):
    sorted_variables["immutable"].append(sorted_variables)
else:
    sorted_variables["mutable"].append(sorted_variables)
