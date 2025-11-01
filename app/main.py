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


def to_sort_variables(variable_map: dict) -> dict:
    result_dict = {
        "mutable": [],
        "immutable": []
    }
    for name, value in variable_map.items():
        if type(value) in (dict, list, set):
            result_dict["mutable"].append(name)
        else:
            result_dict["immutable"].append(name)
    return result_dict


sorted_variables = to_sort_variables({
    "lucky_number": lucky_number,
    "pi": pi,
    "one_is_a_prime_number": one_is_a_prime_number,
    "name": name,
    "my_favourite_films": my_favourite_films,
    "profile_info": profile_info,
    "marks": marks,
    "collection_of_coins": collection_of_coins
})

print(sorted_variables)
sorted_variables = {"mutable": ["my_favourite_films", "marks", "collection_of_coins"],
                    "immutable": ["lucky_number", "pi", "one_is_a_prime_number", "name", "profile_info"]}
