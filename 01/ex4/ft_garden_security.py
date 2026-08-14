#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str,
                 height: float,
                 age: int,
                 growth: float):
        self._name = name
        self._height = height
        self._age_days = age
        self._growth = growth

    def show(self) -> None:
        print(f"{self._name}:",
              f"{self._height}cm,",
              f"{self._age_days} days old",)

    def age(self, days: int = 0) -> None:
        if days < 0:
            print("Negative days is invalid")
            return
        self._age_days += days

    def grow(self, days: int = 1) -> None:
        for _ in range(days):
            self._height = round(self._height + self._growth, 2)

    def set_age(self, new_age: int = 0) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age_days = new_age
        print(f"Age updated: {self._age_days} days")
        return

    def set_height(self, new_height: float = 0) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        print(f"Height updated: {new_height}cm")
        self._height = float(new_height)

    def get_age(self) -> int:
        self.show()
        return self.age

    def get_height(self) -> float:
        self.show()
        return self.height


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10, 0.8)
    print("Plant created: ", end="")
    rose.show()
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-1)
    rose.set_age(-1)
    print("")
    print("Current state: ", end="")
    rose.show()
