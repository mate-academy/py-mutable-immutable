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

variable_names = [
    "lucky_number",
    "pi",
    "one_is_a_prime_number",
    "name",
    "my_favourite_films",
    "profile_info",
    "marks",
    "collection_of_coins",
]

# --------------- Варіант просто з назвами перемінних ---------------------- #
# sorted_variables = {
#     "mutable": ["my_favourite_films", "marks", "collection_of_coins"],
#     "immutable": ["lucky_number", "pi", "one_is_a_prime_number", "name",
#     "profile_info"]
# }

# -------------------- Варіант зі значеннями перемінних  ------------------- #
# ------------------- з обмеженням Flake8 у 79 символів на строку -----------#
sorted_variables = {
    "mutable": [["The Shawshank Redemption",
                 "The Lord of the Rings: The Return of the King",
                 "Pulp Fiction", "The Good, the Bad and the Ugly",
                 "The Matrix"], {"John": 4, "Sergio": 3}, {1, 2, 25}],
    "immutable": [777, 3.14, False, "Richard",
                  ("michel", "michel@gmail.com", "12345678")]
}
