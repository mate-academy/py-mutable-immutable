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
assert type(lucky_number) == int
assert type(pi) == float
assert type(one_is_a_prime_number) == bool
assert type(name) == str
assert type(profile_info) == tuple

assert type(my_favourite_films) == list
assert type(marks) == dict
assert type(collection_of_coins) == set

sorted_variables = dict(mutable=[my_favourite_films, marks,
                                 collection_of_coins], immutable=[lucky_number, pi,
                                                                  one_is_a_prime_number,
                                                                  name, profile_info])
