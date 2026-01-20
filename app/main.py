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

new_list = []
new_list.append(lucky_number)
new_list.append(pi)
new_list.append(one_is_a_prime_number)
new_list.append(name)
new_list.append(my_favourite_films)
new_list.append(profile_info)
new_list.append(marks)
new_list.append(collection_of_coins)

sorted_variables = {
    "mutable": [],
    "immutable": []
}


for i in new_list:
    if isinstance(i, (list, dict, set)):
        sorted_variables["mutable"].append(i)
    else:
        sorted_variables["immutable"].append(i)
