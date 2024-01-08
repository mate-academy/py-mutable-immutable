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


# write your code here

def create_dictionary(**args) -> dict:
    sorted_variables = {"mutable": [],
                        "immutable": []}
    for key, value in args.items():
        if isinstance(value, (list, dict, set)) is True:
            sorted_variables['mutable'].append(key)
        else:
            sorted_variables['immutable'].append(key)

    return sorted_variables


result = create_dictionary(lucky_number=777,
                           pi=3.14,
                           one_is_a_prime_number=False,
                           name="Richard",
                           my_favourite_films=[
                               "The Shawshank Redemption",
                               "The Lord of the Rings: The Return of the King",
                               "Pulp Fiction",
                               "The Good, the Bad and the Ugly",
                               "The Matrix",
                           ],
                           profile_info=("michel", "michel@gmail.com", "12345678"),
                           marks={
                               "John": 4,
                               "Sergio": 3,
                           },
                           collection_of_coins={1, 2, 25})
print(result)
