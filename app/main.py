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

def sorted_variables_func(*args):
    types = {"mutable" : ["list", "dict", "set"],
             "immutable" : ["int", "float", "str", "bool", "tuple"]}

    variables_dict = {key : value for key, value in globals().items()
                      if not key.startswith("__")}

    mutable = []
    immutable = []

    for arg in args:
        var_name = [key for key, value in variables_dict.items()
                    if value is arg]
        if var_name:
            var_name = var_name[0]
            if type(arg).__name__ in types["mutable"]:
                mutable.append(arg)
            elif type(arg).__name__ in types["immutable"]:
                immutable.append(arg)

    return {"mutable" : mutable, "immutable" : immutable}


sorted_variables = sorted_variables_func(lucky_number, pi,
                                         one_is_a_prime_number, name,
                                         my_favourite_films, profile_info,
                                         marks, collection_of_coins)
