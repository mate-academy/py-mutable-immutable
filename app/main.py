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

<<<<<<< HEAD
sorted_variables = {
    "mutable": [my_favourite_films, marks, collection_of_coins],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info]
}

=======
list_of_variables = [lucky_number, pi, one_is_a_prime_number, name,
                     my_favourite_films, profile_info, marks,
                     collection_of_coins]

sorted_variables = {
    "mutable": [],
    "immutable": []
}

for i in list_of_variables:
    if isinstance(i, dict) or isinstance(i, list) or isinstance(i, set):
        sorted_variables["mutable"].append(i)
    sorted_variables["immutable"].append(i)

print(sorted_variables)

# write your code here
>>>>>>> 1ad111165578d80ff3e007b9d7f87414bc8d4c09
