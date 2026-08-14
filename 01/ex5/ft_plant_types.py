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
        print(f"{self._name.capitalize()}:",
              f"{self._height}cm,",
              f"{self._age_days} days old",)
        return

    def age(self, days: int = 0) -> None:
        if days < 0:
            print("Negative days is invalid")
            return
        self._age_days += days
        return

    def grow(self, days: int = 1) -> None:
        for _ in range(days):
            self._height = round(self._height + self._growth, 2)
        return

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
        return

    def get_age(self) -> int:
        self.show()
        return self._age_days

    def get_height(self) -> float:
        self.show()
        return self._height


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth: float,
                 color: str,
                 bloomed: bool = False):
        super().__init__(name, height, age, growth)
        self._color = color
        self._bloomed = bloomed

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed is False:
            print(f" {self._name.capitalize()} has not bloomed yet")
        else:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        return

    def bloom(self):
        print(f"[asking the {self._name.lower()} to bloom]")
        self._bloomed = True
        self.show()
        return


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth: float,
                 trunk_diameter: float):
        super().__init__(name, height, age, growth)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")
        return

    def produce_shade(self):
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name.capitalize()} now produces", end="")
        print(f" a shade of {self._height}cm long and ", end="")
        print(f"{self._trunk_diameter}cm wide.")
        return


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth: float,
                 harvest_season: str,
                 nutritional_value: int = 0):
        super().__init__(name, height, age, growth)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")
        return

    def grow(self, days: int = 1) -> None:
        super().age(days)
        super().grow(days)
        print(f"[make {self._name.lower()} grow and age for {days} days]")
        self._nutritional_value += days
        self.show()
        return


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 0.8, "red")
    rose.show()
    rose.bloom()
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.8, 5.0)
    oak.show()
    oak.produce_shade()
    print("")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    tomato.show()
    tomato.grow(20)
