"""creat func sorted_variables"""

lucky_number, pi, one_is_a_prime_number, name = 777, 3.14, False, "Richard"

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


def sorted_variables(*args, **kwargs) -> dict:
    """
    create dictioanry with with mutable and immutable value
    """
    result_dict = {"mutable": [], "immutable": []}
    lst_args = [args] + [kwargs]
    for el in lst_args:
        if isinstance(el, (int, float, str, tuple, bool)):
            if isinstance(el, int):
                result_dict.setdefault("immutable", []).append("lucky_number")
            elif isinstance(el, float):
                result_dict.setdefault("immutable", []).append("pi")
            elif isinstance(el, str):
                result_dict.setdefault("immutable", []).append("name")
            elif isinstance(el, bool):
                result_dict.setdefault("immutable", []).append("one_is_a_prime_number")
            if isinstance(el, tuple):
                result_dict.setdefault("immutable", []).append("profile_info")

        else:
            if isinstance(el, list):
                result_dict.setdefault("mutable", []).append("my_favourite_films")
            elif isinstance(el, dict):
                result_dict.setdefault("mutable", []).append("marks")
            elif isinstance(el, set):
                result_dict.setdefault("mutable", []).append("collection_of_coins")
    return sorted(result_dict)


sorted_variables(lucky_number,
                 pi,
                 one_is_a_prime_number,
                 name,
                 my_favourite_films,
                 profile_info,
                 marks,
                 collection_of_coins)
