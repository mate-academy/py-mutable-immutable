# Заданные переменные
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

# Словарь для классификации переменных
sorted_variables = {
    "mutable": [],
    "immutable": [],
}

# Список переменных для классификации
data_objects = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]

# Проверка переменных и их классификация
for data_item in data_objects:
    if isinstance(data_item, (list, dict, set)):
        # Если объект изменяемый
        sorted_variables["mutable"].append(data_item)
    elif isinstance(data_item, (int, float, bool, str, tuple)):
        # Если объект неизменяемый
        sorted_variables["immutable"].append(data_item)

# Вывод результата
print(sorted_variables)
