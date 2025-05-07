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

# Lista de todas as variáveis para facilitar a iteração
all_vars = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins
]

# Classificação das variáveis em "mutable" e "immutable"
sorted_variables = {
    "mutable": [var for var in all_vars if isinstance(var, (list, dict, set))],
    "immutable": [var for var in all_vars if isinstance(var, (int, float, str, tuple, bool))]
}

# Exibindo o resultado
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(sorted_variables)