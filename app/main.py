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


def find_value_type(value):
    if type(value) in (str, float, int, bool, tuple):
        sorted_variables["immutable"].append(value)
    elif value is None:
        sorted_variables["immutable"].append(value)
    if type(value) in (list, dict, set):
        sorted_variables["mutable"].append(value)


find_value_type(lucky_number)
find_value_type(pi)
find_value_type(one_is_a_prime_number)
find_value_type(name)
find_value_type(my_favourite_films)
find_value_type(profile_info)
find_value_type(marks)
find_value_type(collection_of_coins)
