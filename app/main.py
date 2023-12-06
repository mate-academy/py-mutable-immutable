lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

# write your code here
def sorted_variables(*args) -> dict:
    variable_name = ["lucky_number", "pi", "one_is_a_prime_number", "name", "my_favourite_films", "profile_info",
                     "marks", "collection_of_coins"]
    variable_name_dict = dict(zip(variable_name, args))
    immutable = []
    mutable = []
    result_dic = {}
    for k, v in variable_name_dict.items():
        if isinstance(v, (int, float, str, bool, tuple, type(None))):
            immutable.append(k)
            result_dic["mutable"] = mutable
        else:
            mutable.append(k)
            result_dic["immutable"] = immutable
    return result_dic



print(sorted_variables(lucky_number, pi, one_is_a_prime_number, name, my_favourite_films,profile_info,marks, collection_of_coins))