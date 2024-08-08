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


def is_mutable(*args) -> list:
    mutable_list = []
    immutable_list = []

    for arg in args:
        if isinstance(arg, (list, set, dict)):
            mutable_list.append(arg)
            continue
        immutable_list.append(arg)

    return [mutable_list, immutable_list]


result_list = (is_mutable(lucky_number, pi, one_is_a_prime_number,
               name, my_favourite_films, profile_info,
               marks, collection_of_coins))

sorted_variables = {"mutable": result_list[0], "immutable": result_list[1]}
