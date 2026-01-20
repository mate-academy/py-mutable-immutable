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

def sorted_variables(values):
    mutable_types = (list, set, dict)
    immutable_types = (int, float, str, tuple, bool)
    sorted_values = {"mutable": [], "immutable": []}
    for i in values:
        if isinstance(i, mutable_types):
            sorted_values["mutable"].append(i)
        elif isinstance(i, immutable_types):
            sorted_values["immutable"].append(i)
    return sorted_values

all_values = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]
sorted_variables = sorted_variables(all_values)

print(sorted_variables)
