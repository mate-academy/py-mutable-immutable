# app/main.py
lucky_number = 777  # entero (immutable)
pi = 3.14  # float (immutable)
one_is_a_prime_number = False  # bool (immutable)
name = "Richard"  # cadena (immutable)

my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]  # lista (mutable)

profile_info = ("michel", "michel@gmail.com", "12345678")  # tupla (immutable)
marks = {"John": 4, "Sergio": 3}  # diccionario (mutable)
collection_of_coins = {1, 2, 25}  # conjunto (mutable)

sorted_variables = {
    "mutable": [my_favourite_films, marks, collection_of_coins],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info]
}
