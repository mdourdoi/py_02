class Plant:
    """Represent a plant with its informations"""

    def __init__(self, name: str, age: int) -> None:
        """Initializes the plant with secured data"""
        self.__name = name
        if (age >= 0):
            self.__age = age
        else:
            print(f"Invalid initialization attempted : age {age}")
            self.__age = 0
            print("Security : age can't be negative, set to 0")

    def get_name(self) -> str:
        """Secures the access to the name"""
        return (self.__name)

    def get_age(self) -> int:
        """Secures the access to the age"""
        return (self.__age)


class GardenError(Exception):
    """Basic error for garden problem"""
    pass


class PlantError(GardenError):
    """Basic error for plans problem"""
    pass


class WaterError(GardenError):
    """Basic error for watering problem"""
    pass


def check_wilting(plant: Plant) -> None:
    """Tests if the plant is wilting"""
    if plant.get_age() >= 15:
        raise PlantError(f"The {plant.get_name()} plant is wilting!")
    else:
        print("Plant is fine!")


def check_watering(watering: int, stock: int) -> None:
    """Checks if you can water the plant"""
    if watering > stock:
        raise WaterError("Not enough water in the tank!")
    else:
        print("Watering is ok!")


def test_error_types() -> None:
    """Catches custom errors"""
    print("=== Custom Garden Errors Demo ===")
    print()
    tomato = Plant("tomato", 20)
    print("Testing PlantError...")
    try:
        check_wilting(tomato)
    except PlantError as cur_error:
        print(f"Caught PlantError: {cur_error}")
        print()
    print("Testing WaterError...")
    try:
        check_watering(30, 20)
    except WaterError as cur_error:
        print(f"Caught WaterError: {cur_error}")
        print()
    print("Testing catching all garden errors...")
    try:
        check_wilting(tomato)
    except GardenError as cur_error:
        print(f"Caught a garden error: {cur_error}")
    try:
        check_watering(30, 20)
    except GardenError as cur_error:
        print(f"Caught a garden error: {cur_error}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
