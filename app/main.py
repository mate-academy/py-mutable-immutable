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

for var_name in dir():
    if not var_name.startswith("__"):
        var = globals()[var_name]
        if isinstance(var, (list, dict, set)):
            sorted_variables["mutable"].append(var)
        elif isinstance(var, (int, float, bool, str, tuple)):
            sorted_variables["immutable"].append(var)

print(sorted_variables)

#  Якщо випадково неправильно зрозумiв завдання, будь ласка вiдпишiть в git