
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

 #write your code here
def is_immutable(var):
    return not isinstance(var, (list, dict, set)) and var is not None

sorted_variables = {"mutable": [], "immutable": []}

globals_copy = dict(globals())

for var_name, var_value in globals_copy.items():
    if is_immutable(var_value):
        sorted_variables["immutable"].append(var_value)
    else:
        sorted_variables["mutable"].append(var_value)

print(sorted_variables)






