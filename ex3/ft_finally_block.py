class EmptyStringError(Exception):
    """Error for empty string"""
    pass


def check_empty(plant: str | None) -> None:
    """Raises an EmptyStringError if the string is empty"""
    if plant is None:
        raise EmptyStringError(plant)
    if len(plant) == 0:
        raise EmptyStringError("[empty name]")


def water_plants(plant_list: list[str | None]) -> None:
    """Tries to water all the plants"""
    print("Opening watering system")
    error = False
    try:
        for plant in plant_list:
            check_empty(plant)
            print(f"Watering {plant}")
    except EmptyStringError as cur_error:
        error = True
        raise EmptyStringError(
            f"Error: Cannot water {cur_error} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
        if not (error):
            print("Watering completed successfully!")


def test_watering_system() -> None:
    """Checks if the watering system always closes as intended"""
    print("=== Garden Watering System ===")
    print()
    try:
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print()
        print("Testing with error...")
        water_plants(["tomato", None])
    except EmptyStringError as cur_error:
        print(cur_error)
    finally:
        print()
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
