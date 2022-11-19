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


def kor(*args) -> dict:

    if type(*args) == list or type(*args) == dict or type(*args) == set:
        sorted_variables["mutable"].append(*args)
    else:
        sorted_variables["immutable"].append(*args)
    return sorted_variables
    pass


kor(lucky_number)
kor(pi)
kor(one_is_a_prime_number)
kor(name)
kor(my_favourite_films)
kor(profile_info)
kor(marks)
kor(collection_of_coins)
