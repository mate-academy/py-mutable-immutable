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

vars_dict = locals().copy()
sorted_variables = {"mutable": [], "immutable": []}
mutable_types = [list, set, dict]
for key, value in vars_dict.items():
    if not key.startswith("__"):
        category = "mutable" if type(vars_dict[key]) in mutable_types \
            else "immutable"
        sorted_variables[category].append(vars_dict[key])
