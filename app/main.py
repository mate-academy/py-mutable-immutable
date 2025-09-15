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

mutable_types = (list, dict, set, bytearray)

sorted_variables = {"mutable": [], "immutable": []}

for _name, _value in globals().items():
    if (_name.startswith("__") and _name.endswith("__")) or _name.startswith("_") or _name == "sorted_variables":
        continue
    category = "mutable" if isinstance(_value, mutable_types) else "immutable"
    sorted_variables[category].append(_value)
