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


def add_dictionary_by_type(args):
    if type(args) in (int, str, bool, float, tuple):
        sorted_variables["immutable"].append(args)
    else:
        sorted_variables["mutable"].append(args)


add_dictionary_by_type(lucky_number)
add_dictionary_by_type(pi)
add_dictionary_by_type(one_is_a_prime_number)
add_dictionary_by_type(name)
add_dictionary_by_type(my_favourite_films)
add_dictionary_by_type(profile_info)
add_dictionary_by_type(marks)
add_dictionary_by_type(collection_of_coins)
# print(sorted_variables)
