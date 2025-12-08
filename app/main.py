# Variables
lucky_number = 7
pi = 3.14
one_is_a_prime_number = False
name = "Samuel"

my_favourite_films = ["Interstellar", "Inception", "The Matrix"]
profile_info = {"age": 18, "country": "Colombia"}
marks = (5, 4, 5)
collection_of_coins = {50, 100, 200}

# Lista correcta según los tests
sorted_variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]


def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())

