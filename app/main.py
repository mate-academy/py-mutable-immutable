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


mutable = dict, set, list
immutable = int, float, str, tuple, bool
sorted_variables = {"mutable": [], "immutable": []}

datas = [lucky_number, pi, one_is_a_prime_number, name,
         my_favourite_films, profile_info, marks, collection_of_coins]

for elem in datas:
    if type(elem) in mutable:
        sorted_variables["mutable"].append(elem)
    if type(elem) in immutable:
        sorted_variables["immutable"].append(elem)
print(sorted_variables)
