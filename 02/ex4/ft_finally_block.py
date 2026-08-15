#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for i in plants:
            water_plant(i)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()

    print("Testing valid plants...")
    plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(plants)
    print()

    print("Testing invalid plants...")
    plants = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(plants)
    print()

    print("Cleanup always happens, even with errors!")
