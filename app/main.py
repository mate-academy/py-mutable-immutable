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

# Визначення списку відсортованих змінних
sorted_variables = {
    "mutable": [
        my_favourite_films,  # list
        marks,  # dict
        collection_of_coins,  # set
    ],
    "immutable": [
        lucky_number,  # int
        pi,            # float
        one_is_a_prime_number, # bool
        name,          # str
        profile_info,  # tuple
    ]
}



# Перевірка, чи 1 є простим числом
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Виконання перевірок і друк значень
if is_prime(1):
    print("1 is not a prime number (This is correct).")
else:
    print("1 is a prime number (This is incorrect).")

print(f"Richard's first favorite film: {my_favourite_films[0]}")
print(f"Number of films in the list: {len(my_favourite_films)}")

print(f"Michel's username: {profile_info[0]}")
print(f"Michel's email: {profile_info[1]}")

print(f"John's marks: {marks['John']}")
print(f"Average marks (assuming numerical values): {sum(marks.values()) / len(marks)}")

print(f"Unique coin values: {collection_of_coins}")
total_coin_value = sum(collection_of_coins)
print(f"Total value of coins: {total_coin_value}")
