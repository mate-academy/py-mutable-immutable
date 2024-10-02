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


def categorize_variables() -> dict[str, list]:
    sorted_variables = {
        "mutable": [],
        "immutable": []
    }

    def add_var_to_category(variable_data: any) -> None:
        if isinstance(variable_data, (list, dict, set)):
            sorted_variables["mutable"].append(variable_data)
        else:
            sorted_variables["immutable"].append(variable_data)

    add_var_to_category(lucky_number)
    add_var_to_category(pi)
    add_var_to_category(one_is_a_prime_number)
    add_var_to_category(name)
    add_var_to_category(my_favourite_films)
    add_var_to_category(profile_info)
    add_var_to_category(marks)
    add_var_to_category(collection_of_coins)

    return sorted_variables


sorted_variables = categorize_variables()
print(sorted_variables)
