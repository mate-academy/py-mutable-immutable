integer_value = 123
empty_list = []
greeting_text = "Hi!"
number_list = [1, 2]
coordinates_tuple = (4, 5)
unique_numbers_set = {6, 7}
data_dictionary = {"key": "value"}
pi_value = 3.14

mutable_list = []
immutable_list = []

# Classifying variables
variables = [
    integer_value, empty_list, greeting_text, number_list,
    coordinates_tuple, unique_numbers_set, data_dictionary, pi_value
]
for item in variables:
    if isinstance(item, (list, dict, set)):
        mutable_list.append(item)
    else:
        immutable_list.append(item)
sorted_variables = {
    "mutable": mutable_list,
    "immutable": immutable_list
}
print(sorted_variables)
