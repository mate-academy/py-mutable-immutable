# immutable values
immutable_int = 123
lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
greeting = "Hi"
name = "Richard"
profile_info = ("michel", "michel@gmail.com", "12345678")  # tuple is immutable
collection_of_coins = (1, 2, 25)  # tuple (3 items, immutable)

# mutable values
mutable_list_empty = []
mutable_list_numbers = [1, 2]
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings",
    "The Return of the King",
    "Pulp Fiction",
    "The Good the Bad and the Ugly",
]  # 4 items
marks = {"John": 4, "Sergio": 3}  # 6 items

# sorted_variables groups mutable and immutable values
sorted_variables = {
    "mutable": [
        mutable_list_empty,
        mutable_list_numbers,
        my_favourite_films,
        marks
    ],
    "immutable": [
        immutable_int,
        greeting,
        lucky_number,
        pi,
        one_is_a_prime_number,
        name,
        profile_info,
        collection_of_coins,
    ],
}
