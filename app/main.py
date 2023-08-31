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

variables = {"lucky_number": lucky_number,
             "pi": pi,
             "one_is_a_prime_number": one_is_a_prime_number,
             "name": name,
             "my_favourite_films": my_favourite_films,
             "profile_info": profile_info,
             "marks": marks,
             "collection_of_coins": collection_of_coins}

sorted_variables = {}
mutable_list = []
immutable_list = []

for key, value in variables.items():
    if isinstance(value, (list, set, dict)):
        mutable_list.append(value)
    else:
        immutable_list.append(value)

sorted_variables["mutable"] = mutable_list
sorted_variables["immutable"] = immutable_list

print(sorted_variables)
