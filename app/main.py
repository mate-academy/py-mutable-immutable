
def ismutable(var_name) -> bool:

    if isinstance(var_name, int | float | str | bool | tuple):
        return False
    return True


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
mutable_list = []
immutable_list = []

if ismutable(lucky_number):
    mutable_list.append(lucky_number)
else:
    immutable_list.append(lucky_number)
if ismutable(pi):
    mutable_list.append(pi)
else:
    immutable_list.append(pi)
if ismutable(one_is_a_prime_number):
    mutable_list.append(one_is_a_prime_number)
else:
    immutable_list.append(one_is_a_prime_number)
if ismutable(name):
    mutable_list.append(name)
else:
    immutable_list.append(name)
if ismutable(my_favourite_films):
    mutable_list.append(my_favourite_films)
else:
    immutable_list.append(my_favourite_films)
if ismutable(profile_info):
    mutable_list.append(profile_info)
else:
    immutable_list.append(profile_info)
if ismutable(marks):
    mutable_list.append(marks)
else:
    immutable_list.append(marks)
if ismutable(collection_of_coins):
    mutable_list.append(collection_of_coins)
else:
    immutable_list.append(collection_of_coins)

sorted_variables = {
    "mutable": mutable_list,
    "immutable": immutable_list
}
