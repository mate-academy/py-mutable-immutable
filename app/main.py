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

List = [lucky_number, pi, one_is_a_prime_number, name, my_favourite_films,
        profile_info, marks, collection_of_coins]

mu = (list, dict, set)
im = (int, float, bool, str, tuple)

sorted_variables = {"mutable": [], "immutable": []}
for current_var in List:
    var_type = type(current_var)
    if var_type in mu:
        sorted_variables["mutable"].append(current_var)
    if var_type in im:
        sorted_variables["immutable"].append(current_var)
