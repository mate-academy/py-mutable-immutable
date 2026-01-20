# immutable data types
lucky_number: int = 777
pi: float = 3.14
one_is_a_prime_number: bool = False
name: str = "Richard"
profile_info: tuple = ("michel", "michel@gmail.com", "12345678")

# mutable data types
my_favourite_films: list = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
marks: dict = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins: set = {1, 2, 25}

sorted_variables = dict(
    immutable=[lucky_number, pi, one_is_a_prime_number, name, profile_info, ],
    mutable=[my_favourite_films, marks, collection_of_coins, ],
)
