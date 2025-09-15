"""Classify module-level variables into mutable vs immutable by inspecting globals()."""

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

# Helper types (prefixed underscore so they are skipped)
_mutable_types = (list, dict, set, bytearray)

# Take a snapshot of current globals to avoid mutating during iteration
_items_snapshot = list(globals().items())

mutable_list = []
immutable_list = []

for _name, _value in _items_snapshot:
    # Skip dunder names and helper names (prefixed with _), and any future key
    if (_name.startswith("__") and _name.endswith("__")) or _name.startswith("_") or _name == "sorted_variables":
        continue
    (mutable_list if isinstance(_value, _mutable_types) else immutable_list).append(_value)

sorted_variables = {"mutable": mutable_list, "immutable": immutable_list}
