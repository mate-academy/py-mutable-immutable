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

all_variables = [lucky_number, pi, one_is_a_prime_number, name,
                 my_favourite_films, profile_info, marks, collection_of_coins]

mutable_variables = []
immutable_variables = []

for obj in all_variables:
    if isinstance(obj, (list, dict, set)):
        mutable_variables.append(obj)
    else:
        immutable_variables.append(obj)

sorted_variables = {"mutable": mutable_variables,
                    "immutable": immutable_variables}
