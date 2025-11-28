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

# write your code here
sorted_variables {
    "mutable" == [],
    "immutable" == []
};
sorted_variables["mutable"].append(collection_of_coins)
sorted_variables["mutable"].append(marks)
sorted_variables["mutable"].append(profile_info)
sorted_variables["mutable"].append(my_favourite_films)
# write your cod here
sorted_variables["immutable"].append(name)
sorted_variables["immutable"].append(one_is_a_prime_number)
sorted_variables["immutable"].append(pi)
sorted_variables["immutable"].append(lucky_number)

return sorted_variables
