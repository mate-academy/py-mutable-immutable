# Задаємо змінні
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

# Створюємо словник sorted_variables
sorted_variables = {"mutable": [], "immutable": []}

# Розподіляємо змінні за категоріями
for var in [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]:
    if isinstance(var, (list, dict, set)):  # Перевіряємо, чи змінна є змінною
        sorted_variables["mutable"].append(var)
    else:  # Інакше додаємо до незмінних
        sorted_variables["immutable"].append(var)

# Вивід результату
print(sorted_variables)

