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

# Объявляем переменные с правильными значениями
lucky_number = 777  # int (immutable)
pi = 3.14  # float (immutable)
one_is_a_prime_number = False  # bool (immutable)
name = "Richard"  # str (immutable)
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]  # list (mutable)
profile_info = ("michel", "michel@gmail.com", "12345678")  # tuple (immutable)
marks = {"John": 4, "Sergio": 3}  # dict (mutable)
collection_of_coins = {1, 2, 25}  # set (mutable)

# Определяем изменяемые и неизменяемые типы данных
mutable_types = (list, set, dict)  # изменяемые
immutable_types = (int, float, str, tuple, bool)  # неизменяемые

# Создаём словарь sorted_variables
sorted_variables = {
    "mutable": [],
    "immutable": []
}

# Добавляем переменные в словарь, используя их ИМЕНА
variables = {
    "lucky_number": lucky_number,
    "pi": pi,
    "one_is_a_prime_number": one_is_a_prime_number,
    "name": name,
    "my_favourite_films": my_favourite_films,
    "profile_info": profile_info,
    "marks": marks,
    "collection_of_coins": collection_of_coins,
}

# Классифицируем переменные
for var_name, var_value in variables.items():
    if isinstance(var_value, mutable_types):
        sorted_variables["mutable"].append(var_value)
    else:
        sorted_variables["immutable"].append(var_value)

# Вывод результата (для проверки)
print(sorted_variables)
