# Washing Station

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

You own a car washing station. Washing cost calculation 
takes a lot of time, and you decide to automate this
calculation. The washing cost will depend on car comfort 
class, car cleanness degree, wash station average rating
and wash station distance from the center of the city.

Create class `Car`, its constructor takes and stores
3 arguments:
1. `comfort_class` - comfort class of a car, from 1 to 7
2. `clean_mark` - car cleanness mark, from very 
dirty - 1 to absolute clean - 10
3. `brand` - brand of the car

Create class `CarWashStation`, its constructor takes and
stores 4 arguments:
1. `distance_from_city_center` - how far station from
the city center, from 1.0 to 10.0
2. `clean_power` - `clean_mark` to which this car wash station
washes (yes, not all stations can clean your car completely)
3. `average_rating` - average rating of the station,
from 1.0 to 5.0, rounded to 1 decimal
4. `count_of_ratings` - number of people who rated

`CarWashStation` should have such methods: 
1. `serve_cars` - method, that takes a list of `Car`'s, washes only
cars with `clean_mark` < `clean_power` of wash station
and returns income of CarWashStation for serving this list of Car's, 
rounded to 1 decimal
2. `calculate_washing_price` - method, that calculates cost for a 
single car wash,
cost is calculated as: car's comfort class * difference between
wash station's clean power and car's clean mark * car wash station 
rating / car wash station 
distance to the center of the city, returns number rounded 
to 1 decimal
3. `wash_single_car` - every car after wash is clean, so it should 
have `clean_mark` equals wash station's `clean_power`, 
make individual method for this.
4. `rate_service` - method to add a single rate.

You can add own methods if you need.

Example:
```python
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

ws = CarWashingStation(6, 8, 3.9, 11)

income = ws.serve_cars([
    bmw,
    audi,
    mercedes
])

income == 41.6

bmw.clean_mark == 8
audi.clean_mark == 9  
mercedes.clean_mark == 8
# audi wasn't washed
# all other cars are washed to '8'

ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)  
# only calculating cost, not washing
wash_cost == 11.7
ford.clean_mark == 1 

ws.rate_service(5)

ws.count_of_ratings == 12
ws.average_rating == 4.0
```