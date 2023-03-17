class Person:
    people = {}
    def __int__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(name=name["name"],
                             age=name["age"]) for name in people]


    for person in people:
        if "wife" in person:
            if person["wife"] is not None:
                Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] is not None:
                Person.people[person["name"]].husband = Person.people[person["husband"]]

    return list_of_people

















# lucky_number = 777
# pi = 3.14
# one_is_a_prime_number = False
# name = "Richard"
# # my_favourite_films = [
# #     "The Shawshank Redemption",
# #     "The Lord of the Rings: The Return of the King",
# #     "Pulp Fiction",
# #     "The Good, the Bad and the Ugly",
# #     "The Matrix",
# # ]
# # profile_info = ("michel", "michel@gmail.com", "12345678")
# # marks = {
# #     "John": 4,
# #     "Sergio": 3,
# # }
# # collection_of_coins = {1, 2, 25}
# #
# # # write your code here
# # sorted_variables = {
# #     "mutable": [my_favourite_films, marks, collection_of_coins],
# #     "immutable": [lucky_number, pi, one_is_a_prime_number, name, profile_info]
# # }
