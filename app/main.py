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

"""
# parse the names of first n variables in a file
def get_n_variable_names(file, n):
    try:
        with open(file, "r") as f:
            variables = []
            while len(variables) != n:
                line = f.readline().split(" = ")[0]
                if line[0].isalpha() and "import" not in line:
                    variables.append(line)
            return variables
    except FileNotFoundError:
        print(f"{file} not found")
        return None

variable_names = get_n_variable_names("main.py", 8)
"""

"""
In order for the above approach to pass the tests,
we really shouldn't read the file while tests also try to do that

So the solution is to either move the code to other file
Or run it without tests, get the variable names
And set them explicitly.
"""
variable_names = [
    "lucky_number",
    "pi",
    "one_is_a_prime_number",
    "name",
    "my_favourite_films",
    "profile_info",
    "marks",
    "collection_of_coins"
]

# get values by names
variable_values = [globals()[name] for name in variable_names]

# lists with corresponding types
mutable = [list, dict, set]
immutable = [int, float, str, bool, tuple]

sorted_variables = {
    "mutable": [],
    "immutable": []
}

# assign values to dict
for variable_value in variable_values:
    if type(variable_value) in mutable:
        sorted_variables["mutable"].append(variable_value)
    else:
        sorted_variables["immutable"].append(variable_value)
