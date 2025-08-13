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

def sort_varibles(*args) -> dict:
    sorted_variables = {}
    mutable_types = (list, dict, set)

    for var in args:
        if type(var) in mutable_types:
            if 'mutable' not in sorted_variables:
                sorted_variables['mutable'] = [var]
            else:
                sorted_variables['mutable'].append(var)
        else:
            if 'immutable' not in sorted_variables:
                sorted_variables['immutable'] = [var]
            else:
                sorted_variables['immutable'].append(var)

    return sorted_variables

sorted_variables = sort_varibles(
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
)

print(sorted_variables)