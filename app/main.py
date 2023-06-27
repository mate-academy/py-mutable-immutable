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


variables = [ ("lucky_number", 777),
        ("pi", 3.14),
        ("one_is_a_prime_number", False),
        ("name", "Richard"),
        (
            "my_favourite_films",
            [
                "The Shawshank Redemption",
                "The Lord of the Rings: The Return of the King",
                "Pulp Fiction",
                "The Good, the Bad and the Ugly",
                "The Matrix",
            ],
        ),
        ("profile_info", ("michel", "michel@gmail.com", "12345678")),
        ("marks", {"John": 4, "Sergio": 3}),
        ("collection_of_coins", {1, 2, 25}),
    ]


sorted_variables = {"mutable": [], "immutable": []}

for i in variables:
    if type(i[1]) in [int, float, str, bool, tuple]:
        sorted_variables["immutable"].append(i[0])
    else:
        sorted_variables["mutable"].append(i[0])
print(sorted_variables)
