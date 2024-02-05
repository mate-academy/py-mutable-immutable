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


local_variables = locals().copy()
mutable_list = []
immutable_list = []

sorted_variables = {
    "mutable": mutable_list,
    "immutable": immutable_list
}

for key, value in local_variables.items():
    if key.startswith("__") and key.endswith("__"):
        continue
    if (isinstance(value, list)
            or isinstance(value, dict)
            or isinstance(value, set)):
        mutable_list.append(value)
    else:
        immutable_list.append(value)

print(sorted_variables)
