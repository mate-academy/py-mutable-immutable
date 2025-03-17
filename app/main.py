# Variáveis fornecidas
a = 123
b = []
c = "Oi!"
d = [1, 2]
e = (1, 2)
f = {1, 2}
g = 3.14
h = {"chave": "valor"}

# Variáveis extras exigidas pelo teste
lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix"
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {"John": 4, "Sergio": 3}
collection_of_coins = {1, 2, 25}  # ✅ Corrigido!

# Função para verificar se uma variável é mutável ou imutável
def eh_mutavel(obj):
    try:
        hash(obj)
        return False
    except TypeError:
        return True
print("my_favourite_films =", repr(my_favourite_films))
# Criação do dicionário com as variáveis classificadas
sorted_variables = {
    "mutable": [var for var in [b, d, f, h, my_favourite_films, marks, collection_of_coins] if eh_mutavel(var)],
    "immutable": [var for var in [a, c, e, g, lucky_number, pi, one_is_a_prime_number, name, profile_info] if not eh_mutavel(var)]
}
# Exibir resultado (opcional)
print(sorted_variables)
