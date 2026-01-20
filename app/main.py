lucky_number = 777 # int (imultavel)
pi = 3.14 #int (imultavel)
one_is_a_prime_number = False #bool imultavel
name = "Richard" #str imultavel
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
] #list multavel
profile_info = ("michel", "michel@gmail.com", "12345678") # tuple imultavel
marks = {
    "John": 4,
    "Sergio": 3,
}  #dict multavel
collection_of_coins = {1, 2, 25}
#set multavel
sorted_variables = {
    "mutable": [my_favourite_films, marks, collection_of_coins],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info]
}
print(sorted_variables)
