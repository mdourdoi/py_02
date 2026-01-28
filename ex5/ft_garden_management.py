class EmptyStringError(Exception):
    """Error for empty string"""
    pass


class GardenError(Exception):
    """Basic error for garden problem"""
    pass


class PlantError(GardenError):
    """Basic error for plans problem"""
    pass


class WaterError(PlantError):
    """Basic error for watering problem"""
    pass


class SunlightError(PlantError):
    """Basic error for watering problem"""
    pass


class Plant:
    """Represent a plant with its informations.
    Corrupted data is intentionally possible"""

    def __init__(
            self,
            name: str,
            water_level: int,
            sunlight_hours: int) -> None:
        """Initializes the plant with secured data"""
        self.__name = name
        self.__sunlight_hours = sunlight_hours
        self.__water_level = water_level

    def get_name(self) -> str:
        """Secures the access to the name"""
        return (self.__name)

    def get_sunlight_hours(self) -> int:
        """Secures the access to the sunlight hours"""
        return (self.__sunlight_hours)

    def get_water_level(self) -> int:
        """Secures the access to the sunlight hours"""
        return (self.__water_level)

    def set_water_level(self, water_level: int) -> None:
        """Sets the water level"""
        self.__water_level = water_level

    def set_sunlight_hours(self, sunlight_hours: int) -> None:
        """Sets the sunlight hours"""
        self.__sunlight_hours = sunlight_hours


class Garden:
    """Represents a garden with plants"""

    def __init__(self, *plants: Plant) -> None:
        """Initializes the garden with secured data"""
        self.__plants = {}
        for plant in plants:
            self.add_plant(plant)

    def get_plants(self) -> dict[str, Plant]:
        """Securely gets the list of plants"""
        return (self.__plants)

    def has_plant(self, plant: Plant) -> bool:
        """Checks if the plant is in the garden"""
        if (isinstance(plant, Plant)):
            key = plant.get_name()
            if (key in self.get_plants()):
                return (True)
        return (False)

    def add_plant(self, plant: Plant) -> None:
        """Securely adds a plant to the garden"""
        if (self.has_plant(plant)):
            raise GardenError(
                f"{plant.get_name().capitalize()} is already in the garden")
        else:
            self.__plants[plant.get_name()] = plant

    def remove_plant(self, plant: Plant) -> None:
        """Securely removes a plant from the garden"""
        if (self.has_plant(plant)):
            self.__plants.pop(plant.get_name())
        else:
            print("The plant is not in the garden")


class GardenManager:
    """Represent a Garden manager with its informations.
    This is where errors are managed"""

    @staticmethod
    def check_empty(string: str | None) -> None:
        """Raises an EmptyStringError if the string is empty"""
        if string is None:
            raise EmptyStringError(string)
        if len(string) == 0:
            raise EmptyStringError("empty")

    @staticmethod
    def check_water_supply(watering: int, stock: int) -> None:
        """Checks if you can water the plant"""
        if watering > stock:
            raise WaterError("Not enough water in the tank!")
        else:
            print("Watering is ok!")

    @staticmethod
    def check_plant_health(plant: Plant) -> None:
        """Checks variables for a plant and raises an error when needed"""
        water = plant.get_water_level()
        sunlight = plant.get_sunlight_hours()
        if water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        if water < 1:
            raise WaterError(f"Water level {water} is too low (min 1)")
        if sunlight > 12:
            raise SunlightError(
                f"Sunlight hours {sunlight} is too high (max 12)")
        if sunlight < 2:
            raise SunlightError(
                f"Sunlight hours {sunlight} is too low (min 2)")
        print(f"{plant.get_name()}: healthy (water: {water}, sun: {sunlight})")

    def __init__(self, garden: Garden, water_tank: int) -> None:
        """Initializes the manager with secured data"""
        self.__garden = garden
        if water_tank >= 0:
            self.__water_tank = water_tank
        else:
            self.__water_tank = 0
            print("Error : Tank supply cannot have a negative value, set to 0")

    def get_tank(self) -> int:
        """Get the amount of water available in the water_tank"""
        return self.__water_tank

    def add_plants_to_garden(self, *plants: Plant) -> None:
        """Adds a plant to the garden"""
        print("Adding plants to garden...")
        target = self.__garden
        error = False
        try:
            for plant in plants:
                self.check_empty(plant.get_name())
                target.add_plant(plant)
                name = plant.get_name()
                print(f"Added {name} successfully")
        except (GardenError, EmptyStringError) as cur_error:
            print(f"Error adding plant: Plant name cannot be {cur_error}!")
            error = True
        finally:
            print("Done adding plants!")
            if error:
                print("An error occured, not all plants were added")
            if not error:
                print("All plant are added to the garden!")

    def watering_plant(self, watering: int) -> None:
        """Tries to water the plants
        if there is more stock than water used to watering.
        Catches a GardenError rather than a WaterError
        if there is not enough water because the subject's example said so"""
        try:
            self.check_water_supply(watering, self.get_tank())
        except GardenError as cur_error:
            print(f"Caught GardenError: {cur_error}")
            return
        try:
            print("Watering plants...")
            print("Opening watering system")
            target = self.__garden.get_plants().values()
            try:
                for plant in target:
                    self.check_empty(plant.get_name())
                    print(f"Watering {plant.get_name()} - success")
            except EmptyStringError as cur_error:
                print(f"Error: Cannot water {cur_error} - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_garden_health(self) -> None:
        """Checks the health of each plant in the garden"""
        print("Checking plant health...")
        target = self.__garden.get_plants().values()
        error = False
        try:
            for plant in target:
                self.check_plant_health(plant)
        except PlantError as cur_error:
            print(f"Error checking {plant.get_name()}: {cur_error}")
            error = True
        finally:
            print("Health check done!")
            if not error:
                print("All plants are fine!")


def test_garden_management():
    """Checks securities on the GardenManager"""
    print("=== Garden Management System ===")
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 15, 8)
    empty_name = Plant("", 5, 5)
    garden = Garden()
    garden_manager = GardenManager(garden, 20)
    print()
    garden_manager.add_plants_to_garden(tomato, lettuce, empty_name)
    print()
    garden_manager.watering_plant(10)
    print()
    garden_manager.check_garden_health()
    print()
    print("Testing error recovery...")
    garden_manager.watering_plant(25)
    print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
