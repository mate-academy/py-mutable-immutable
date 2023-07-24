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


def sort_variables() -> dict:
    __doc__
    "immutale_varisables = []"


a, b, c = my_favourite_films, marks, collection_of_coins
q, w, e, r, t = lucky_number, pi, one_is_a_prime_number, name, profile_info

mutable_variables = []
immutale_varisables = []
mutable_variables = [a, b, c]
immutale_varisables = [q, w, e, r, t]
sort_variables()
mu = mutable_variables
im = immutale_varisables
sorted_variables = {"mutable": mu, "immutable": im}
print(sorted_variables)
