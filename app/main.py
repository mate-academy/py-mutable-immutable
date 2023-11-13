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
# write code below this line
list_of_all_variable = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
]
sorted_variables = {}
mutable_variable_list = []
immutable_variable_list = []
for element in list_of_all_variable:
    if isinstance(element, (int, str, bool, float, tuple)):
        immutable_variable_list.append(element)
    else:
        mutable_variable_list.append(element)
sorted_variables["mutable"] = mutable_variable_list
sorted_variables["immutable"] = immutable_variable_list
