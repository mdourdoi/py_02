def check_temperature(temp_str: str):
    """Tries to convert the input into an int"""
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")
    if 0 <= temp <= 40:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    else:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")


def test_temperature_input() -> None:
    """Tests the check_temperature function"""
    tests = ["25", "abc", "100", "-50"]
    for i in tests:
        print(f"Testing temperature: {i}")
        try:
            check_temperature(i)
        except ValueError as cur_error:
            print(cur_error)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
