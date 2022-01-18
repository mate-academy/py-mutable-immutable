import pytest

from app.main import Car, CarWashStation


def test_car():
    bmw = Car(2, 3, "BMW")
    assert bmw.comfort_class == 2, "Class Car should store 'comfort_class'"
    assert bmw.clean_mark == 3, "Class Car should store 'clean_mark'"
    assert bmw.brand == "BMW", "Class Car should store 'brand'"


@pytest.mark.parametrize(
    "cars,washstation,total_cost",
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
def test_car_wash_station(cars, washstation, total_cost):
    income = washstation.serve_cars(cars)
    assert income == total_cost, f"Income should equal to {total_cost}"


@pytest.mark.parametrize(
    "cars,washstation,cars_clean_marks",
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
def test_car_is_washed(cars, washstation, cars_clean_marks):
    income = washstation.serve_cars(cars)
    assert [car.clean_mark for car in cars] == cars_clean_marks, (
        f"Car should keep his 'clear_mark' if it >= 'clear_power' of wash station, "
        f"otherwise it should equal to 'clear_power'"
    )


@pytest.mark.parametrize(
    "car,washstation,mark",
    [
        (Car(2, 1, "Ford"), CarWashStation(3, 10, 4.2, 11), 1),
        (Car(4, 5, "Audi"), CarWashStation(6, 8, 3.9, 11), 5),
        (Car(3, 3, "BMW"), CarWashStation(2, 9, 4.8, 13), 3),
    ],
)
def test_car_cost_check_not_washed(car, washstation, mark):
    cost = washstation.calculate_washing_price(car)
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
