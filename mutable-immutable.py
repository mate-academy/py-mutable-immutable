lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = ["The Shawshank Redemption", "Green Mile", "Fight Club"]
profile_info = ("michael", "michael@gmail.com", "12345")
marks = {
    "english": 3,
    "history": 4,
}
collection_of_coins = {1, 2, 25}

sorted_variables = {
    "mutable": [my_favourite_films, marks, collection_of_coins],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info],
}

print(len(sorted_variables["mutable"]) + len(sorted_variables["immutable"]))