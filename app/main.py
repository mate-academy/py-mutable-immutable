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

# Variáveis fornecidas
a = 123              # int (imutável)
b = []               # list (mutável)
c = "Hi!"            # str (imutável)
d = [1, 2]           # list (mutável)
e = (1, 2)           # tuple (imutável)
f = {"key": "value"} # dict (mutável)
g = {1, 2}           # set (mutável)
h = True             # bool (imutável)

# Classificação das variáveis em "mutable" e "immutable"
sorted_variables = {
    "mutable": [var for var in [a, b, c, d, e, f, g, h] if isinstance(var, (list, dict, set))],
    "immutable": [var for var in [a, b, c, d, e, f, g, h] if isinstance(var, (int, float, str, tuple, bool))]
}

# Exibindo o resultado
print(sorted_variables)
