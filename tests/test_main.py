import pytest
import inspect

import app.main


@pytest.mark.parametrize(
    "variable_name",
    [
        "lucky_number",
        "pi",
        "one_is_a_prime_number",
        "name",
        "my_favourite_films",
        "profile_info",
        "marks",
        "collection_of_coins",
        "sorted_variables",
    ],
)
def test_variables_should_be_defined(variable_name):
    assert hasattr(
        app.main, variable_name
    ), f"Variable '{variable_name}' should be defined."


@pytest.mark.parametrize(
    "variable,value",
    [
        ("lucky_number", 777),
        ("pi", 3.14),
        ("one_is_a_prime_number", False),
        ("name", "Richard"),
        (
            "my_favourite_films",
            [
                "The Shawshank Redemption",
                "The Lord of the Rings: The Return of the King",
                "Pulp Fiction",
                "The Good, the Bad and the Ugly",
                "The Matrix",
            ],
        ),
        ("profile_info", ("michel", "michel@gmail.com", "12345678")),
        ("marks", {"John": 4, "Sergio": 3}),
        ("collection_of_coins", {1, 2, 25}),
    ],
)
def test_variables_values(variable, value):
    assert (
        getattr(app.main, variable) == value
    ), f"Variable '{variable}' should be equal to {value}."


@pytest.mark.parametrize(
    "variable_name",
    [
        "lucky_number",
        "pi",
        "one_is_a_prime_number",
        "name",
        "my_favourite_films",
        "profile_info",
        "marks",
        "collection_of_coins",
    ],
)
def test_variables_should_be_added_to_sorted_variables(variable_name):
    sorted_variables = getattr(app.main, "sorted_variables")
    assert (
        getattr(app.main, variable_name) in sorted_variables["mutable"] or
        getattr(app.main, variable_name) in sorted_variables["immutable"]
    ), f"Variable '{variable_name}' should be added to 'sorted_variables'"


def is_immutable(obj):
    if isinstance(obj, (int, str, bool, float, tuple)):
        return True
    return False


def test_variables_added_to_the_correct_list():
    sorted_variables = getattr(app.main, "sorted_variables")
    for variable in sorted_variables["mutable"]:
        assert is_immutable(variable) is False, (
            f"{variable} should be in 'immutable' list"
        )

    for variable in sorted_variables["immutable"]:
        assert is_immutable(variable) is True, (
            f"{variable} should be in 'mutable' list"
        )


def test_removed_comment():
    with open(app.main.__file__, "r") as f:
        lines = inspect.getsource(app.main)
        assert "# write your code here" not in lines
