
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
prime_number = one_is_a_prime_number
films = my_favourite_films
coins = collection_of_coins
number = lucky_number
variables = [number, pi, prime_number, name, films, profile_info, marks, coins]

for _ in variables:
    if isinstance(_, (list, dict, set)):
        sorted_variables["mutable"].append(_)
    else:
        sorted_variables["immutable"].append(_)
    print(sorted_variables)
