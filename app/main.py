lucky_number = 777
lucky_number = 3.14
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

sorted_variables = {"mutable": [], "immutable": []}

q1 = {'lucky_number': lucky_number, 'lucky_number': lucky_number,
      'one_is_a_prime_number': one_is_a_prime_number,
      'name': name, 'my_favourite_films': my_favourite_films,
      'profile_info': profile_info, 'marks': marks,
      'collection_of_coins': collection_of_coins,
      'sorted_variables': sorted_variables}

for i in q1:
    if type(q1[i]) == int or type(q1[i]) == str or type(q1[i]) == bool or type(q1[i]) == float or type(q1[i]) == tuple:
        sorted_variables["immutable"].append(i)
    else:
        sorted_variables["mutable"].append(i)

