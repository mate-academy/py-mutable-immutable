# Check Your Code Against the Following Points

## Code Style

1. If you have some long math, you can split it onto additional variables, 
or break after binary operations (not before - it cause the W504 errors)

Good example:

```python
fuel_consumption = max_fuel_consumption * height_fuel_consumption_coeficient
estimated_speed = plan_max_speed - wind_awerage_speed * wind_angle_coefisient
estimated_time = distance_to_the_destinatoin / estimated_speed
how_much_fuel_needed = fuel_consumption * estimated_time * overlap_coeficient
```

Good example:

```python
how_much_fuel_needed = (max_fuel_consumption
                        * height_fuel_consumption_coeficient
                        * distance_to_the_destinatoin
                        / (plan_max_speed
                           - wind_awerage_speed
                           * wind_angle_coefisient)
                        * overlap_coeficient)
```

Bad example:

```python
how_much_fuel_needed = max_fuel_consumption \
                       * height_fuel_consumption_coeficient \
                       * distance_to_the_destinatoin / (
                               plan_max_speed 
                               - wind_awerage_speed 
                               * wind_angle_coefisient
                       ) * overlap_coeficient
```

2. Use descriptive and correct variable names.

Good example:

```python
def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"
```

Bad example:
```python
def get_full_name(x: str, y: str) -> str:
    return f"{x} {y}"
```

## Clean Code

1. You can avoid else when have return statement.

Good example:

```python
def is_adult(age: int) -> str:
    if age >= 18:
        return "adult"
    return "not an adult"
```

Bad example:

```python
def is_adult(age: int) -> str:
    if age >= 18:
        return "adult"
    else:
        return "not an adult"
```

2. Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
