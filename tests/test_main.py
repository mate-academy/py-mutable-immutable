from unittest.mock import patch
import pytest
import os

from app.main import Car, CarWashStation


def test_car():
    bmw = Car(2, 3, "BMW")
    assert bmw.comfort_class == 2, "Class Car should store 'comfort_class'"
    assert bmw.clean_mark == 3, "Class Car should store 'clean_mark'"
    assert bmw.brand == "BMW", "Class Car should store 'brand'"


@pytest.mark.parametrize(
    "cars,wash_station,total_cost",
    [
        ([], CarWashStation(3, 9, 4.4, 144), 0),
        ([Car(2, 1, "Ford")], CarWashStation(3, 9, 4.2, 11), 22.4),
        ([Car(2, 9, "Ford")], CarWashStation(3, 8, 4.2, 11), 0),
        (
            [Car(3, 3, "BMW"), Car(4, 5, "Audi"), Car(7, 1, "Mercedes")],
            CarWashStation(6, 7, 3.9, 11),
            40.3,
        ),
        (
            [Car(3, 3, "BMW"), Car(4, 5, "Audi"), Car(7, 9, "Mercedes")],
            CarWashStation(6, 7, 3.9, 11),
            13.0,
        ),
        (
            [Car(3, 8, "BMW"), Car(4, 8, "Audi"), Car(7, 9, "Mercedes")],
            CarWashStation(6, 7, 3.9, 11),
            0,
        ),
    ],
)
def test_car_wash_station(cars, wash_station, total_cost):
    income = wash_station.serve_cars(cars)
    assert income == total_cost, f"Income should equal to {total_cost}"

def test_wash_single_car_is_called():
    with patch.object(CarWashStation, 'wash_single_car') as mock_method:
        CarWashStation(3, 9, 4, 11).serve_cars([Car(2, 1, "Ford")])
        assert mock_method.called, "Expected 'wash_single_car' to have " \
                                   "been called inside 'serve_cars' method"


@pytest.mark.parametrize(
    "cars,wash_station,cars_clean_marks",
    [
        ([Car(2, 1, "Ford")], CarWashStation(3, 9, 4.2, 11), [9]),
        ([Car(2, 9, "Ford")], CarWashStation(3, 8, 4.2, 11), [9]),
        (
            [Car(3, 3, "BMW"), Car(4, 5, "Audi"), Car(7, 1, "Mercedes")],
            CarWashStation(6, 7, 3.9, 11),
            [7, 7, 7],
        ),
        (
            [Car(3, 3, "BMW"), Car(4, 5, "Audi"), Car(7, 9, "Mercedes")],
            CarWashStation(2, 8, 4.8, 13),
            [8, 8, 9],
        ),
    ],
)
def test_car_is_washed(cars, wash_station, cars_clean_marks):
    wash_station.serve_cars(cars)
    assert [car.clean_mark for car in cars] == cars_clean_marks, (
        f"Car should keep his 'clear_mark' if it >= 'clear_power' of wash station, "
        f"otherwise it should equal to 'clear_power'"
    )


@pytest.mark.parametrize(
    "car,wash_station,mark",
    [
        (Car(2, 1, "Ford"), CarWashStation(3, 10, 4.2, 11), 1),
        (Car(4, 5, "Audi"), CarWashStation(6, 8, 3.9, 11), 5),
        (Car(3, 3, "BMW"), CarWashStation(2, 9, 4.8, 13), 3),
    ],
)
def test_car_cost_check_not_washed(car, wash_station, mark):
    wash_station.calculate_washing_price(car)
    assert car.clean_mark == mark, (
        f"Method 'calculate_washing_price' should not change" f"'car.clean_mark'"
    )


@pytest.mark.parametrize(
    "init_avg_rating,init_num_ratings,mark,result_avg_rating,result_num_ratings",
    [
        (2.2, 2, 5, 3.1, 3),
        (2.4, 11, 5, 2.6, 12),
        (3.8, 7, 2, 3.6, 8),
        (4.4, 42, 4, 4.4, 43),
    ],
)
def test_rate_service(
    init_avg_rating, init_num_ratings, mark, result_avg_rating, result_num_ratings
):
    ws = CarWashStation(2, 9, init_avg_rating, init_num_ratings)
    ws.rate_service(mark)
    assert ws.average_rating == result_avg_rating, (
        f"'average_rating' should equal to {result_avg_rating}, "
        f"when initial 'average_rating' was {init_avg_rating}, "
        f"and initial 'count_of_ratings' was {init_num_ratings}"
    )
    assert ws.count_of_ratings == result_num_ratings, (
        f"'count_of_ratings' should equal to {result_num_ratings}, "
        f"when initial 'count_of_ratings' was {init_num_ratings}"
    )


def test_unnecessary_comment():
    if os.path.exists(os.path.join(os.pardir, "app", "main.py")):
        main_path = os.path.join(os.pardir, "app", "main.py")
    else:
        main_path = os.path.join("app", "main.py")

    with open(main_path, "r") as main:
        main_content = main.read()

        assert (
                "# write your code here" not in main_content
        ), "Remove unnecessary comment"

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
