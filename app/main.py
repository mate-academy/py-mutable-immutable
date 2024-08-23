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
all_changers = [lucky_number, pi, one_is_a_prime_number, name, my_favourite_films, profile_info, collection_of_coins,
                marks]
change_type = [list, dict, set]
sorted_variables = {
    "mutable": [],
    "immutable": []
}
for changers in all_changers:
    if type(changers) in change_type:
        sorted_variables["mutable"].append(changers)
    else:
        sorted_variables["immutable"].append(changers)
print(sorted_variables)
