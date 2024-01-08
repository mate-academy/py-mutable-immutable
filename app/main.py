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

list_of_different_type_variable = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
]

sorted_variables = {"mutable": [], "immutable": []}
mutable_data = [dict, list, set]
for data in list_of_different_type_variable:
    type_of_variable = type(data)
    if type_of_variable in mutable_data:
        sorted_variables["mutable"].append(data)
        continue
    sorted_variables["immutable"].append(data)
