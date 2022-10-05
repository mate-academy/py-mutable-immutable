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

mutable_klass = (list, dict, set)
immutable_klass = (int, float, bool, str, tuple)
mutable_list = []
immutable_list = []
variables_list = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]

for i in range(len(variables_list)):
    if isinstance(variables_list[i], mutable_klass):
        mutable_list.append(variables_list[i])
    else:
        immutable_list.append(variables_list[i])

sorted_variables = {"mutable": mutable_list, "immutable": immutable_list}
