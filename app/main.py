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

lucky_number_2 = lucky_number + 2
pi_2 = pi + 2
one_is_a_prime_number_2 = True
name_2 = name
name_2 += " Kowalski"
my_favourite_films_2: list = my_favourite_films

profile_information = list(profile_info)
profile_information[0] += " cors"
profile_info_2 = tuple(profile_information)

marks_2 = marks
marks_2["John"] = 4

collection_of_coins_2 = collection_of_coins
collection_of_coins_2.add(1)

data_types = [lucky_number, pi, one_is_a_prime_number, name,
              my_favourite_films, profile_info, marks, collection_of_coins]
data_types_2 = [lucky_number_2, pi_2, one_is_a_prime_number_2, name_2,
                my_favourite_films_2, profile_info_2, marks_2,
                collection_of_coins_2]

sorted_variables: dict[str, list] = {"mutable": [], "immutable": []}

for i in range(len(data_types)):
    original = data_types[i]
    after_change = data_types_2[i]

    if original is after_change:
        sorted_variables["mutable"].append(original)
    else:
        sorted_variables["immutable"].append(original)

print(sorted_variables)
