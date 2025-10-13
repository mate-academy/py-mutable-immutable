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

# 8 variáveis de diferentes tipos de dados
idade = 25                     # int
altura = 1.75                  # float
mensagem = "Olá, mundo!"       # str
coordenadas = (10, 20)         # tuple
numeros = [1, 2, 3, 4]         # list
conjunto_itens = {5, 6, 7}     # set
dados_pessoa = {"nome": "Ana", "idade": 30}  # dict
ativo = True                   # bool

# Dicionário separando variáveis mutáveis e imutáveis
# Dicionário agrupando as variáveis originais por mutabilidade

sorted_variables = {
    "mutable": [my_favourite_films, marks, collection_of_coins],
    "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info]
}


print(sorted_variables)
