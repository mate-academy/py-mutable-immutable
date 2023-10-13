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

list_of_variables = [lucky_number, pi, one_is_a_prime_number,
                     name, my_favourite_films, profile_info,
                     marks, collection_of_coins]
list_of_mutable = []
list_of_immutable = []
sorted_variables = {"mutable": list_of_mutable,
                    "immutable": list_of_immutable}
for element in list_of_variables:
    if isinstance(element, (list, set, dict)):
        list_of_mutable.append(element)
    else:
        list_of_immutable.append(element)

sorted_variables_manual = {
    "mutable": [my_favourite_films, marks, collection_of_coins],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info]
}
