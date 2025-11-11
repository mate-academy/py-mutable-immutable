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

sorted_values = {"mutable":[], "immutable":[]}
if isinstance(lucky_number,(list,dict,set)):
    sorted_values["mutable"].append("lucky_number")
else:
    sorted_values["immutable"].append("lucky_number")
if isinstance(pi,(list,dict,set)):
    sorted_values["mutable"].append("pi")
else:
    sorted_values["immutable"].append("pi")   
if isinstance(one_is_a_prime_number,(list,dict,set)):
    sorted_values["mutable"].append("one_is_a_prime_number")
else:
    sorted_values["immutable"].append("one_is_a_prime_number")
if isinstance(name,(list,dict,set)):
    sorted_values["mutable"].append("name")
else:
    sorted_values["immutable"].append("name")
if isinstance(my_favourite_films,(list,dict,set)):
    sorted_values["mutable"].append("my_favourite_films")
else:
    sorted_values["immutable"].append("my_favourite_films")
if isinstance(profile_info,(list,dict,set)):
    sorted_values["mutable"].append("profile_info")
else:
    sorted_values["immutable"].append("profile_info")
if isinstance(marks,(list,dict,set)):
    sorted_values["mutable"].append("marks")
else:
    sorted_values["immutable"].append("marks")
if isinstance(collection_of_coins,(list,dict,set)):
    sorted_values["mutable"].append("collection_of_coins")
else:
    sorted_values["immutable"].append("collection_of_coins")
print(sorted_values)

