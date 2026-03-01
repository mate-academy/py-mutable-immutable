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

# # write your code here
# Your task is to create dictionary `sorted_variables` with two keys:
# # `"mutable"` and `"immutable"`.
# Each value should be equal to a list that contains all variables \
# of corresponding type.

variables = [lucky_number, pi, one_is_a_prime_number, name, 
             my_favourite_films, profile_info, marks, collection_of_coins]

sorted_variables = {"mutable": [], "immutable": []}

for var in variables:
    try:
        hash(var)
        sorted_variables["immutable"].append(var)
    except TypeError:
        sorted_variables["mutable"].append(var)
