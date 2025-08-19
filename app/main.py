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

resultado = {
    "mutable": [],
    "immutable": []
}

for idx, var in enumerate(resultado["mutable"], start=1):
    letra = chr(96 + idx)  # 97 é 'a' na tabela ASCII
    print(f"  {letra}) {var[0]} = {var[1]} ({var[2]})")

for idx, var in enumerate(resultado["immutable"], start=1):
    letra = chr(96 + idx)
    print(f"  {letra}) {var[0]} = {var[1]} ({var[2]})")