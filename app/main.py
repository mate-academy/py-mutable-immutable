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


list_of_variables = [
    {"lucky_number": 777},
    {"pi": 3.14},
    {"one_is_a_prime_number": False},
    {"name": "Richard"},
    {"my_favourite_films": [
        "The Shawshank Redemption",
        "The Lord of the Rings: The Return of the King",
        "Pulp Fiction",
        "The Good, the Bad and the Ugly",
        "The Matrix"
    ]},
    {"profile_info": ("michel", "michel@gmail.com", "12345678")},
    {"marks": {"John": 4, "Sergio": 3}},
    {"collection_of_coins": {1, 2, 25}}
]

sorted_variables = {"mutable": [], "immutable": []}
for char in list_of_variables:
    for key, value in char.items():
        if type(value) == list or type(value) == dict or type(value) == set:
            sorted_variables["mutable"].append(value)
        elif (type(value) == int or type(value) == float or type(value) == str
              or type(value) == bool or type(value) == tuple):
            sorted_variables["immutable"].append(value)

