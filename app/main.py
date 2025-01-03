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


types_dictionary = {
    "lucky_number" : lucky_number,
    "pi" : pi,
    "one_is_a_prime_number" : one_is_a_prime_number,
    "name" : name,
    "my_favourite_films" : my_favourite_films,
    "profile_info" : profile_info,
    "marks" : marks,
    "collection_of_coins" : collection_of_coins
}
sorted_variables = {}

for key in types_dictionary:
    new_list = []
    if type(types_dictionary[key]) in [str, int, float, tuple, bool]:
        key_name = "immutable"
    else:
        key_name = "mutable"

    if f"{key_name}" in sorted_variables :
        new_list = sorted_variables[f"{key_name}"].copy()
        new_list.append(types_dictionary[key])
        sorted_variables.update({f"{key_name}" : new_list})
    else:
        new_list.append(types_dictionary[key])
        sorted_variables.update({f"{key_name}" : new_list})
