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
def create_dictionary(*args) -> dict:
    mut_list = []
    immut_list = []

    for i in range(len(args)):

        if isinstance(args[i], (list, dict, set)):
            mut_list.extend([args[i]])
        if isinstance(args[i], (int, float, str, tuple, bool)):
            immut_list.extend([args[i]])

    sorted_variables = {"mutable": [mut_list], "immutable": [immut_list]}

    return sorted_variables
