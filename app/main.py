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

mutable_vars = []
immutable_vars = []

immutable_vars.append(lucky_number)
immutable_vars.append(pi)
immutable_vars.append(one_is_a_prime_number)
immutable_vars.append(name)
immutable_vars.append(profile_info)

mutable_vars.append(my_favourite_films)
mutable_vars.append(marks)
mutable_vars.append(collection_of_coins)

sorted_variables = {}
sorted_variables["mutable"] = mutable_vars
sorted_variables["immutable"] = immutable_vars
