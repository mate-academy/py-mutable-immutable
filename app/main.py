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

sorted_variables = {
    "mutable": [],
    "immutable": []
}


def sort_variables(current_var: any) -> None:

    if isinstance(current_var, (int, float, str, bool, tuple)):
        sorted_variables["immutable"].append(current_var)
    else:
        sorted_variables["mutable"].append(current_var)


sort_variables(lucky_number)
sort_variables(pi)
sort_variables(one_is_a_prime_number)
sort_variables(name)
sort_variables(my_favourite_films)
sort_variables(profile_info)
sort_variables(marks)
sort_variables(collection_of_coins)

print(sorted_variables)
