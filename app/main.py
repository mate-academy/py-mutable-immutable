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
# 8 variáveis de diferentes tipos
a = 42                  # int (imutável)
b = "ChatGPT"           # str (imutável)
c = [1, 2, 3]           # list (mutável)
d = (4, 5)              # tuple (imutável)
e = {"chave": "valor"}  # dict (mutável)
f = {1, 2, 3}           # set (mutável)
g = 3.14                # float (imutável)
h = frozenset([4, 5])   # frozenset (imutável)

# Separar variáveis por mutabilidade
sorted_variables = {
    "mutable": [c, e, f],
    "immutable": [a, b, d, g, h]
}

print(sorted_variables)
