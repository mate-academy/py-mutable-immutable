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

dd = {"lucky_number": 777,
      "pi": 3.14,
      "one_is_a_prime_number": False,
      "name": "Richard",
      "my_favourite_films": [
          "The Shawshank Redemption",
          "The Lord of the Rings: The Return of the King",
          "Pulp Fiction",
          "The Good, the Bad and the Ugly",
          "The Matrix",
      ],
      "profile_info": ("michel", "michel@gmail.com", "12345678"),
      "marks": {
          "John": 4,
          "Sergio": 3,
      },
      "collection_of_coins": {1, 2, 25}}


def classify_variables(variables: dict) -> dict:
    mutable_types = (list, dict, set)
    mutable = []
    immutable = []

    for var1 in variables.values():
        if isinstance(var1, mutable_types):
            mutable.append(var1)
        else:
            immutable.append(var1)

    return {"mutable": mutable, "immutable": immutable}


sorted_variables = classify_variables(dd)
