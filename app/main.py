

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


sorted_variables = {"mutable": [], "immutable": []}

def sort_variables(*args) -> None:

    for current_variable in args:
        what_type = str(type(current_variable))
        key = "immutable"

        if "dict" in what_type or "list" in what_type or "set" in what_type:
            key = "mutable"

        sorted_variables[key].append(current_variable)


sort_variables(lucky_number, pi, one_is_a_prime_number)
sort_variables(name, my_favourite_films, profile_info)
sort_variables(marks, collection_of_coins)
