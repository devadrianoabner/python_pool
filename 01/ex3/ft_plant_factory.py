#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str,
                 height: float,
                 age: int,
                 growth: float):
        self.name = name
        self.height = round(height, 1)
        self.age_days = age
        self.growth = round(growth, 1)

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
    rose = Plant("Rose", 25.0, 30, 0.8)
    oak = Plant("Oak", 200.0, 365, 0.1)
    cactus = Plant("Cactus", 5.0, 90, 0.2)
    sunflower = Plant("Sunflower", 80.0, 45, 0.6)
    fern = Plant("Fern", 15.0, 120, 0.4)
    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()
