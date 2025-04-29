lucky_number = 777               # int – liczby całkowite są niemutowalne
pi = 3.14                        # float – liczby zmiennoprzecinkowe są niemutowalne
one_is_a_prime_number = False   # bool – wartości logiczne są niemutowalne
name = "Richard"                # str – ciągi znaków są niemutowalne
profile_info = (
    "michel",
    "michel@gmail.com",
    "12345678",  # tuple – tuples are immutable
)
# Zmienne mutowalne (mutable)
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}  # set – zbiory są mutowalne

sorted_variables = {
    "mutable": [
        my_favourite_films,
        marks,
        collection_of_coins
    ],
    "immutable": [
        lucky_number,
        pi,
        one_is_a_prime_number,
        name,
        profile_info
    ]
}



