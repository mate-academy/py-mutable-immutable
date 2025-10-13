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

# write your code here
# 8 variables of different data types
a = 10                     # int
b = 3.14                   # float
c = "Hello"                # str
d = (1, 2, 3)              # tuple
e = [1, 2, 3]              # list
f = {1, 2, 3}              # set
g = {'x': 1, 'y': 2}       # dict
h = True                   # bool

# Grouping variables by mutability
sorted_variables = {
    "mutable": [e, f, g],
    "immutable": [a, b, c, d, h]
}

print(sorted_variables)
