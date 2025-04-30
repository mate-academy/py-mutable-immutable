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


def sort_variables(*args) -> dict:
    all_dict_types = {"mutable": [], "immutable": []}  # задаємо порожній dict
    immutable_tup = (int, float, str, bool, tuple)  # tuple з immutable
    mutable_tup = (list, dict, set)  # tuple з mutable

    for i in args:  # для кожної змінної у функції
        if type(i) in immutable_tup:  # якщо тип змінної у immutable
            all_dict_types["immutable"].append(i)  # додаємо до ключа immutable
        elif type(i) in mutable_tup:  # якщо тип змінної у mutable
            all_dict_types["mutable"].append(i)  # додаємо до ключа mutable
    return all_dict_types  # повертаємо dict


sorted_variables = sort_variables(  # визначаємо, що сортує функція
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
)
