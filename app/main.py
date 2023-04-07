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
col_of_coins = {1, 2, 25}

variables_list = [lucky_number, pi, one_is_a_prime_number, name,
                  my_favourite_films, profile_info, marks, col_of_coins]
sorted_variables = {}
mutable_type = []
immutable_type = []

for char in variables_list:
    if isinstance(char, (list, dict, set)):
        mutable_type.append(char)
    else:
        immutable_type.append(char)
sorted_variables["mutable"] = mutable_type
sorted_variables["immutable"] = immutable_type
print(sorted_variables)
