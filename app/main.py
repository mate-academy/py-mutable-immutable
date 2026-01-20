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

sorted_variables = {"immutable": [], "mutable": []}
lsim = []
lsim.append(lucky_number)
lsim.append(pi)
lsim.append(one_is_a_prime_number)
lsim.append(name)
lsim.append(profile_info)
sorted_variables["immutable"] = lsim

lsmu = []
lsmu.append(my_favourite_films)
lsmu.append(marks)
lsmu.append(collection_of_coins)
sorted_variables["mutable"] = lsmu
