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

# Присвоєння типів змінним
int_ = int
str_ = str
list_ = list
dict_ = dict
tuple_ = tuple
set_ = set
bool_ = bool

# Додаємо змінні до відповідних списків на основі їх типів
variables = [lucky_number, pi, one_is_a_prime_number, name, my_favourite_films,
             profile_info, marks, collection_of_coins]
mutable_vars = []
immutable_vars = []

for data_item in variables:
    if isinstance(data_item, (list, dict, set)):
        mutable_vars.append(data_item)
    else:
        immutable_vars.append(data_item)

# Створюємо словник зі змінними, розділеними за типами
sorted_variables = {
    "mutable": mutable_vars,
    "immutable": immutable_vars
}

print(sorted_variables)
