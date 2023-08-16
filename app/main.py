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


mutable = [list, dict, set]
immutable = [int, float, str, tuple, bool]

list_of_final_object_mut = []
list_of_final_object_immut = []

all_objects = [
    lucky_number, pi, one_is_a_prime_number,
    name, my_favourite_films, profile_info,
    marks, collection_of_coins
]


for obj in all_objects:
    if type(obj) in [list, dict, set]:
        list_of_final_object_mut.append(obj)
    elif type(obj) in [int, float, str, tuple, bool]:
        list_of_final_object_immut.append(obj)

sorted_variables = {
    "mutable": list_of_final_object_mut,
    "immutable": list_of_final_object_immut
}
