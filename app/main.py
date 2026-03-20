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

mutable_list= []
immutable_list = []
elemets = [lucky_number, pi, one_is_a_prime_number, my_favourite_films, profile_info, marks, collection_of_coins]

def types_detection(): 
    for element in elemets: 
        if type(element) == int or type(element) == float or type(element) == bool or type(element) == tuple:
            immutable_list.append(element)
        else:
            mutable_list.append(element)
    
    return immutable_list, mutable_list

sorted_variable = { 
    "immutable": types_detection()[0], 
    "mutable": types_detection()[1]
}

for key, value in sorted_variable.items(): 
    print("\n")
    print(key, value)
    print("\n")



