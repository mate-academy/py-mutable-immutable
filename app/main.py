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
mutable = []
immutable = []
if isinstance(lucky_number, (int, float, bool, str, tuple)):
    immutable.append(lucky_number)
else:
    mutable.append(lucky_number)
if isinstance(pi, (int, float, bool, str, tuple)):
    immutable.append(pi)
else:
    mutable.append(pi)
if isinstance(one_is_a_prime_number, (int, float, bool, str, tuple)):
    immutable.append(one_is_a_prime_number)
else:
    mutable.append(one_is_a_prime_number)
if isinstance(name, (int, float, bool, str, tuple)):
    immutable.append(name)
else:
    mutable.append(name)
if isinstance(my_favourite_films, (int, float, bool, str, tuple)):
    immutable.append(my_favourite_films)
else:
    mutable.append(my_favourite_films)
if isinstance(profile_info, (int, float, bool, str, tuple)):
    immutable.append(profile_info)
else:
    mutable.append(profile_info)
if isinstance(marks, (int, float, bool, str, tuple)):
    immutable.append(marks)
else:
    mutable.append(marks)
if isinstance(collection_of_coins, (int, float, bool, str, tuple)):
    immutable.append(collection_of_coins)
else:
    mutable.append(collection_of_coins)

sorted_variables = {
    "mutable": mutable,
    "immutable": immutable
}
