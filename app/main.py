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

result = [lucky_number, pi, one_is_a_prime_number, name,
          my_favourite_films, collection_of_coins, profile_info, marks]
chang = []
no_chang = []
for variable_name in result:
    if isinstance(variable_name, (list, set, dict)):
        chang.append(variable_name)
    elif isinstance(variable_name, (int, float, bool, str, tuple)):
        no_chang.append(variable_name)

sorted_variables = {"mutable": chang, "immutable": no_chang}
