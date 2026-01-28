def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int) -> None:
    """Checks all variables for a plant and raises an error when needed"""
    if len(plant_name) == 0:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """Checks if all the tests are working as intended"""
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    check_plant_health("tomato", 5, 5)
    print()
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as cur_error:
        print(f"Error: {cur_error}")
    print()
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as cur_error:
        print(f"Error: {cur_error}")
    print()
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as cur_error:
        print(f"Error: {cur_error}")
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
