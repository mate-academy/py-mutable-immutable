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

def sort_variables_by_mutability():
    mutable_variables = [my_favourite_films, marks, collection_of_coins]  # Lists, dictionaries, and sets are mutable
    immutable_variables = [lucky_number, pi, one_is_a_prime_number, name,
                           profile_info]  # Integers, floats, booleans, strings, and tuples are immutable

    return {"mutable": mutable_variables, "immutable": immutable_variables}


sorted_variables = sort_variables_by_mutability()
print(sorted_variables)
