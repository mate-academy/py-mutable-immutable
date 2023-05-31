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

sorted_variables = {"mutable": [], "immutable": []}


def obj_distributor(arg: object) -> dict:

    check_list = [list, dict, set]

    if type(arg) in check_list:
        sorted_variables["mutable"].append(arg)
    else:
        sorted_variables["immutable"].append(arg)
    return sorted_variables


obj_distributor(lucky_number)
obj_distributor(pi)
obj_distributor(one_is_a_prime_number)
obj_distributor(name)
obj_distributor(my_favourite_films)
obj_distributor(profile_info)
obj_distributor(marks)
obj_distributor(collection_of_coins)
