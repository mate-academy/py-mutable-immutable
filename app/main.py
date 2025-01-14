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

dd = {'lucky_number': 777,
      'pi': 3.14,
      'one_is_a_prime_number': False,
      'name': "Richard",
      'my_favourite_films': [
          "The Shawshank Redemption",
          "The Lord of the Rings: The Return of the King",
          "Pulp Fiction",
          "The Good, the Bad and the Ugly",
          "The Matrix",
      ],
      'profile_info': ("michel", "michel@gmail.com", "12345678"),
      'marks': {
          "John": 4,
          "Sergio": 3,
      },
      'collection_of_coins': {1, 2, 25}}


def classify_variables(variables: dict):
    mutable_types = (list, dict, set)
    mutable = []
    immutable = []

    for var in variables.values():
        if isinstance(var, mutable_types):
            mutable.append(var)
        else:
            immutable.append(var)

    return {"mutable": mutable, "immutable": immutable}


sorted_variables = classify_variables(dd)
