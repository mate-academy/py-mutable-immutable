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


def add_dictionary_by_type(*args) -> None:
    for argument in args:
        if type(argument) in (int, str, bool, float, tuple):
            sorted_variables["immutable"].append(argument)
        else:
            sorted_variables["mutable"].append(argument)


add_dictionary_by_type(lucky_number, pi, one_is_a_prime_number, name)
add_dictionary_by_type(my_favourite_films, profile_info, marks)
add_dictionary_by_type(collection_of_coins)
print(sorted_variables)
