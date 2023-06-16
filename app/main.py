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


mutuable = []
immutuable = []

def mut_immut(my_dict: dict) -> list:
    for key, value in my_dict.items():
        if type(value) == set or type(value) == dict or type(value) == list:
            mutuable.append(key)
        else:
            immutuable.append(key)
        sorted_variables = {
            "mutuable": mutuable,
            "immutuable": immutuable
        }

    return sorted_variables


print(mut_immut(my_dict = {
    "lucky_number": 777,
    "pi":  3.14,
    "one_is_a_prime_number": False,
    "name": "Richard",
    "my_favourite_films": [
        "The Shawshank Redemption",
        "The Lord of the Rings: The Return of the King",
        "Pulp Fiction",
        "The Good, the Bad and the Ugly",
        "The Matrix"],
    "profile_info": ("michel", "michel@gmail.com", "12345678"),
    "marks": {
        "John": 4,
        "Sergio": 3,
    },
    "collection_of_coins": {1, 2, 25}
    }))

