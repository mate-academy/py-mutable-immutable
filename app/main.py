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


def variable_sort(*args) -> dict:
    mutable_list = []
    immutable_list = []
    for arg in args:
        if type(arg) in [int, float, tuple, str, bool]:
            immutable_list.append(arg)
        elif type(arg) in [list, set, dict]:
            mutable_list.append(arg)

    return {"mutable": mutable_list, "immutable": immutable_list}


sorted_variables = variable_sort(lucky_number,
                                 pi,
                                 one_is_a_prime_number,
                                 name,
                                 my_favourite_films,
                                 profile_info,
                                 marks,
                                 collection_of_coins)

print(sorted_variables)
