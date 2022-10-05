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

sorted_variables = {}


def sorted(*args) -> dict:
    for i in args:
        group = "immutable"
        if type(i) == set or type(i) == dict or type(i) == list:
            group = "mutable"

        if group not in sorted_variables:
            sorted_variables[group] = [i]
        else:
            sorted_variables[group].append(i)
    return sorted_variables


print(
    sorted(pi, lucky_number, collection_of_coins, marks, profile_info,
           my_favourite_films, name, one_is_a_prime_number))
