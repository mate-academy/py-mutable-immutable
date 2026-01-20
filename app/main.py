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

list_params = []
list_params.append(lucky_number)
list_params.append(pi)
list_params.append(one_is_a_prime_number)
list_params.append(name)
list_params.append(my_favourite_films)
list_params.append(profile_info)
list_params.append(marks)
list_params.append(collection_of_coins)

sorted_variables = {"mutable" : None, "immutable" : None}

for param in list_params:
    if isinstance(param, (int, float, str, bool, tuple)):
        if sorted_variables["immutable"] is None:
            sorted_variables["immutable"] = [param]
        else:
            sorted_variables["immutable"] += [param]

    else:
        if sorted_variables["mutable"] is None:
            sorted_variables["mutable"] = [param]
        else:
            sorted_variables["mutable"] += [param]
