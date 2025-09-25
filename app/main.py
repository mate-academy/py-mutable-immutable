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
    "John": 9,
    "Sergio": 11,
}
collection_of_coins = {1, 2, 25}

# write your code here

# The 8 variables of different data types
int_var = 1
float_var = 2.5
str_var = "hello"
bool_var = True
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
set_var = {7, 8, 9}
dict_var = {"key": "value"}

# Create the sorted_variables dictionary
sorted_variables = {
    "mutable": [],
    "immutable": []
}

# List of all variables
all_variables = [
    int_var, float_var, str_var, bool_var,
    list_var, tuple_var, set_var, dict_var
]

# Iterate through the variables and sort them
for var in all_variables:
    if isinstance(var, (list, dict, set)):
        sorted_variables["mutable"].append(var)
    else:
        sorted_variables["immutable"].append(var)

# Print the resulting dictionary to verify
print(sorted_variables)