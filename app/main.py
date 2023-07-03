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
list_a = [lucky_number, pi, one_is_a_prime_number, name,
          my_favourite_films, profile_info, marks, collection_of_coins]
list_b = [int, float, complex, bool,
          str, tuple, frozenset]
copy = []
un_copy = []
sorted_variables = {}
for i in range(len(list_a)):
    if type(list_a[i]) in list_b:
        copy.append(list_a[i])
        sorted_variables["immutable"] = copy
    else:
        un_copy.append(list_a[i])
        sorted_variables["mutable"] = un_copy
print(sorted_variables)
