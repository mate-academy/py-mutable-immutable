# Variables
lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"

my_favourite_films = ["Matrix", "Lord of the Rings", "Star Wars"]  # mutable (list)
profile_info = {"age": 30, "country": "USA"}  # mutable (dict)
marks = (5, 4, 3, 5, 5)  # immutable (tuple)
collection_of_coins = {1, 2, 5, 10, 20, 50}  # mutable (set)

# Diccionario requerido por los tests
sorted_variables = {
    "mutable": [
        my_favourite_films,
        profile_info,
        collection_of_coins,
    ],
    "immutable": [
        lucky_number,
        pi,
        one_is_a_prime_number,
        name,
        marks,
    ],
}


def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())



