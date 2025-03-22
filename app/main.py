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
sorted_variables = {"mutable": [], "immutable": []}


def variable_type(variables: list[any]) -> None:
    for ithem in variables:
        if isinstance(ithem, (list, dict, set)):
            sorted_variables["mutable"].append(ithem)
        else:
            sorted_variables["immutable"].append(ithem)


variables_list = [
    lucky_number, pi, one_is_a_prime_number, name,
    my_favourite_films, profile_info, marks, collection_of_coins
]
variable_type(variables_list)
print(sorted_variables)
