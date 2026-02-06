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
data_type_dict = {key:value for key, value in locals().items() if key in ["lucky_number", "pi","one_is_a_prime_number","name", "my_favourite_films", "profile_info", "marks", "collection_of_coins"]}
#Created a dictionary with "Mutable" and Immutable" keys and empty values
sorted_variables = {"mutable":[], "immutable":[]} 

#write your code here
#Create a fucntion that takes any number of data types as arguments
def create_dict(type_dict)-> dict :
    
    for key, value in type_dict.items():
        if isinstance(value, (list, dict, set)):
            sorted_variables["mutable"].append(value)
        else:
            sorted_variables["immutable"].append(value)
        
    return sorted_variables
    
create_dict(data_type_dict) 
       
    