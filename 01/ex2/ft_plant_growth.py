#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str,
                 height: float,
                 age: int,
                 growth: float):
        self.name = name
        self.height = height
        self.age_days = age
        self.growth = growth

    def show(self) -> None:
        print(f"{self.name}:",
              f"{self.height}cm,",
              f"{self.age_days} days old",)

    def age(self, days: int = 0) -> None:
        if days < 0:
            print("Negative days is invalid")
            return
        self.age_days += days

    def grow(self, days: int = 1) -> None:
        for _ in range(days):
            self.height = round(self.height + self.growth, 2)


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Growth ===")
    plant.show()

    initial_height = plant.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.age(1)
        plant.grow(1)
        plant.show()

    total_growth = round(plant.height - initial_height, 2)
    print(f"Growth this week: {total_growth}cm")
