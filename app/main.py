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


sorted_variables = {
    "mutable": [],
    "immutable": []
}


# "змінний"
sorted_variables["mutable"].append([
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix"
])

sorted_variables["mutable"].append({
    "John": 4,
    "Sergio": 3
})

sorted_variables["mutable"].append({1, 2, 25})

# "незмінний"
sorted_variables["immutable"].append(777)
sorted_variables["immutable"].append(3.14)
sorted_variables["immutable"].append(False)
sorted_variables["immutable"].append("Richard")
sorted_variables["immutable"].append(("michel", "michel@gmail.com", "12345678"))
