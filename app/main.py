lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix"
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3
}
collection_of_coins = {1, 2, 25}

sorted_variables = {
    "mutable": [],
    "immutable": []
}

all_variables = {}
all_variables["lucky_number"] = lucky_number
all_variables["pi"] = pi
all_variables["one_is_a_prime_number"] = one_is_a_prime_number
all_variables["name"] = name
all_variables["my_favourite_films"] = my_favourite_films
all_variables["profile_info"] = profile_info
all_variables["marks"] = marks
all_variables["collection_of_coins"] = collection_of_coins

for values_from_all_variables in all_variables.values():
    if type(values_from_all_variables) == int \
            or type(values_from_all_variables) == float \
            or type(values_from_all_variables) == bool \
            or type(values_from_all_variables) == str \
            or type(values_from_all_variables) == tuple:
        sorted_variables["immutable"].append(values_from_all_variables)
    else:
        sorted_variables["mutable"].append(values_from_all_variables)

print(f'{sorted_variables}')
