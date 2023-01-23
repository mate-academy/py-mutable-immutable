#the dict_creation function creates a working dictionary from a list of variables of different types

def dict_creation(**variable):
    global dict_work
    dict_work = dict(variable)
    
#I create an empty dictionary "sorted_variables" with the keys "mutable" and "immutable", the values 
#of this dictionary will be in the form of lists

sorted_variables = {"mutable": [], "immutable": []}

dict_creation(lucky_number = 777,
pi = 3.14,
one_is_a_prime_number = False,
name = "Richard",
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
],
profile_info = ("michel", "michel@gmail.com", "12345678"),
marks = {
    "John": 4,
    "Sergio": 3,
},
collection_of_coins = {1, 2, 25})

#using the for loop, I sort through the dict_work dictionary and fill the sorted_variables dictionary

for key,value in dict_work.items():
    if isinstance (value, (list , set , dict)):
        sorted_variables["mutable"].append(key)
    else:
        sorted_variables["immutable"].append(key)
print(sorted_variables)
