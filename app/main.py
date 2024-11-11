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


sorted_variables = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    collection_of_coins,
]

print(f"Name: {name}")
print(f"Profile Info: {profile_info}")

total_coin_value = sum(collection_of_coins)
print("Total value of coins:", total_coin_value)

student_name = "John"
if student_name in marks:
    print(f"{student_name}'s mark:", marks[student_name])
else:
    print(f"{student_name} is not in the list.")

