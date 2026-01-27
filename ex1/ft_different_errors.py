def garden_operation(operation: str, operand: str) -> None:
    """Test the operation with given operand"""
    if operation == "convert":
        try:
            int(operand)
        except ValueError:
            raise ValueError("Caught ValueError: invalid literal for int()")
    if operation == "division":
        try:
            try:
                temp = int(operand)
            except ValueError:
                raise ValueError("Caught ValueError: invalid literal for int")
            1 / temp
        except ZeroDivisionError:
            raise ZeroDivisionError(
                "Caught ZeroDivisionError: divison by zero")
    if operation == "file":
        try:
            test = open(operand)
            test.close()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Caught FileNotFoundError: No such file '{operand}'")
    if operation == "key":
        testdict = {"key1": 1, "key2": 2}
        try:
            testdict[operand]
        except KeyError:
            raise KeyError(f"Caught KeyError: '{operand}'")
    else:
        print("Operation not found")
        return
    print("Operation successfull!")


def test_error_types() -> None:
    """Catches errors from garden_operation and displays errors"""
    print("Testing ValueError...")
    try:
        garden_operation("convert", "abc")
    except ValueError as cur_error:
        print(cur_error)
        print()
    print("Testing ZeroDivisionError...")
    try:
        garden_operation("division", "0")
    except ZeroDivisionError as cur_error:
        print(cur_error)
        print()
    print("Testing FileNotFoundError...")
    try:
        garden_operation("file", "missing.txt")
    except FileNotFoundError as cur_error:
        print(cur_error)
        print()
    print("Testing KeyError...")
    try:
        garden_operation("key", "missing\\_plant")
    except KeyError as cur_error:
        print(cur_error.args[0])
        print()
    print("Testing multiple errors together...")
    try:
        garden_operation("convert", "abc")
        garden_operation("division", "0")
        garden_operation("file", "missing.txt")
        garden_operation("key", "missing\\_plant")
    except Exception:
        print("Caught an error, but program continues!")
        print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print()
    test_error_types()
