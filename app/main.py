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


# Imprimindo todos os tipos
print("Lucky number:", lucky_number)
print("Pi value:", pi)
print("Is one a prime number?", one_is_a_prime_number)
print("Name:", name)
print("My favourite films:", my_favourite_films)
print("Profile info:", profile_info)
print("Marks:", marks)
print("Coin collection:", collection_of_coins)

print("\n--- Testando mutabilidade ---")

# Strings são imutáveis: não dá pra modificar diretamente
try:
    name[0] = "B"
except TypeError as e:
    print("Strings são imutáveis → erro:", e)

# Tuplas são imutáveis também
try:
    profile_info[0] = "rafael"
except TypeError as e:
    print("Tuplas são imutáveis → erro:", e)

# Listas são mutáveis
my_favourite_films.append("Fight Club")
print("Filmes atualizados (lista é mutável):", my_favourite_films)

# Dicionários são mutáveis
marks["John"] = 5
print("Notas atualizadas:", marks)

# Conjuntos são mutáveis
collection_of_coins.add(10)
print("Coleção de moedas atualizada:", collection_of_coins)
