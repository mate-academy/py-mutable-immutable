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

def check_type(list_elem : list) -> dict:
    for_mutable = []
    for_immutable = []
    sorted_variables = {}
    for elem in list_elem:
        if isinstance(elem,(int,str,tuple,float)):
            for_immutable.append(elem)
        else:
            for_mutable.append(elem)
    sorted_variables['mutable'] = for_mutable
    sorted_variables['immutable'] = for_immutable
    return sorted_variables
