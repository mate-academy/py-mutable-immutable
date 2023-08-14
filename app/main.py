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

dictionary_variables = {
    "mutable": [list, dict, set],
    "immutable": [int, float, bool, str, tuple]
}

sorted_variables = {
    "mutable": [],
    "immutable": []
}

for key, values in dictionary_variables.items():
    for value in values:
        if value == type(lucky_number):
            sorted_variables[key].append(lucky_number)
        if value == type(pi):
            sorted_variables[key].append(pi)
        if value == type(one_is_a_prime_number):
            sorted_variables[key].append(one_is_a_prime_number)
        if value == type(name):
            sorted_variables[key].append(name)
        if value == type(profile_info):
            sorted_variables[key].append(profile_info)
        if value == type(my_favourite_films):
            sorted_variables[key].append(my_favourite_films)
        if value == type(marks):
            sorted_variables[key].append(marks)
        if value == type(collection_of_coins):
            sorted_variables[key].append(collection_of_coins)
