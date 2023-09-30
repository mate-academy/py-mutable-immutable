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

for_mutable = []
for_immutable = []
general_lst = [profile_info, marks]
sorted_variables = {}
for elem in general_lst:
    if isistance(type(elem(int,str,tuple,float))):
        for_immutable.append(elem)
    else:
        for_mutable.append(elem)
sorted_variables['mutable'] = for_mutable
sorted_variables['immutable'] = for_immutable
print(sorted_variables)
