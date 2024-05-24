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


def is_mutable(var_name: any) -> dict:
    mutable_types = (list, set, dict)
    return isinstance(var_name, mutable_types)


sorted_variables = {
    "mutable": [],
    "immutable": []
}

variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
]

for varname in variables:
    if is_mutable(varname):
        sorted_variables["mutable"].append(varname)
    else:
        sorted_variables["immutable"].append(varname)

print(sorted_variables)
