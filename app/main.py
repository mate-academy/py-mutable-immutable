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

list_with_variables = [lucky_number, pi, one_is_a_prime_number,
                       name, my_favourite_films, profile_info, marks,
                       collection_of_coins]

list_with_mutable_types = [list, set, dict]

sorted_variables = {"mutable": [], "immutable": []}

for i in range(len(list_with_variables)):
    if type(list_with_variables[i]) in list_with_mutable_types:
        sorted_variables["mutable"].append(list_with_variables[i])
    else:
        sorted_variables["immutable"].append(list_with_variables[i])
