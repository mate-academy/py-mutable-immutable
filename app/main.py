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
collection = [lucky_number, pi, one_is_a_prime_number, name,
              my_favourite_films, profile_info, marks, collection_of_coins]
immutable_types = [int, float, bool, str, tuple]
sorted_variables = {
}
for member in collection:
    if type(member) in immutable_types:
        if "immutable" in sorted_variables:
            sorted_variables["immutable"].append(member)
        else:
            sorted_variables["immutable"] = [member]
    else:
        if "mutable" in sorted_variables:
            sorted_variables["mutable"].append(member)
        else:
            sorted_variables["mutable"] = [member]
print(sorted_variables)
