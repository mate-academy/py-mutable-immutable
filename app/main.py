lucky_number = 777  # Immutable (int)
pi = 3.14  # Immutable (float)
one_is_a_prime_number = False  # Immutable (bool)
name = "Richard"  # Immutable (str)
my_favourite_films = (
    "Inception", "The Matrix", "Interstellar"
)  # Immutable (tuple)
profile_info = {
    "name": "John",
    "age": 30,
    "city": "New York"
}  # Mutable (dict)
marks = {
    "John": 4,
    "Alice": 5,
    "Bob": 3
}
collection_of_coins = {1, 2, 5, 10, 20, 50}  # Immutable (frozenset)

mutable_list = []
immutable_list = []

variables = [
    lucky_number, pi, one_is_a_prime_number, name,
    my_favourite_films, profile_info, marks, collection_of_coins
]

for item in variables:
    if isinstance(item, (list, dict, set)):
        mutable_list.append(item)
    else:
        immutable_list.append(item)

sorted_variables = {
    "mutable": [profile_info, marks],
    "immutable": [
        lucky_number,
        pi,
        one_is_a_prime_number,
        name,
        my_favourite_films,
        collection_of_coins]
}

print(sorted_variables)
