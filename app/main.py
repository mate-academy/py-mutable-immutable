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

# Creating dictionary where results will be added
sorted_variables = {
    "mutable" : [],
    "immutable": []}

# Adding all variables to list to iterate through variables
variables_list = [lucky_number,
                  pi,
                  one_is_a_prime_number,
                  name,
                  my_favourite_films,
                  profile_info,
                  marks,
                  collection_of_coins]

# Itterating thgough variables
for item in variables_list:

    # Checking if data type is mutable or immutable
    if type(item) == list or type(item) == dict or type(item) == set:
        sorted_variables["mutable"].append(item)
    else:
        sorted_variables["immutable"].append(item)
