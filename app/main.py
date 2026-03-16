lucky_number: int = 777  # int
pi: float = 3.14  # float
one_is_a_prime_number: bool = False  # bool
name: str = "Richard"  # str
profile_info: tuple = ("michel", "michel@gmail.com", "12345678")  # tuple
my_favourite_films: list = ["The Shawshank Redemption",
                            "The Lord of the Rings:"
                            " The Return"
                            " of the King",
                            "Pulp Fiction", "The Good, the Bad"
                                            " and the Ugly",
                            "The Matrix", ]  # list
marks: dict = {"John": 4, "Sergio": 3, }  # dict
collection_of_coins: set = {1, 2, 25}  # set
sorted_variables = {"mutable": [my_favourite_films, marks,
                                collection_of_coins],
                    "immutable": [lucky_number, pi,
                                  one_is_a_prime_number,
                                  name, profile_info]}
print(sorted_variables)
