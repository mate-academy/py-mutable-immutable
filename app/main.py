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


def sort_variables_by_mutability(*args) -> dict:
    sorted_variables = {"mutable": [], "immutable": []}

    for arg in args:
        sorted_variables["mutable" if isinstance(arg, (list, set, dict)) else "immutable"].append(arg)
        
    return sorted_variables


sorted_variables = sort_variables_by_mutability(lucky_number, pi, one_is_a_prime_number, name, my_favourite_films, profile_info, marks, collection_of_coins)
print(sorted_variables)
