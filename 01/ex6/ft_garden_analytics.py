#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self):
            self._count_grow = 0
            self._count_age = 0
            self._count_show = 0

        def display(self) -> None:
            print(f"Stats: {self._count_grow} grow,",
                  f"{self._count_age} age,",
                  f"{self._count_show} show")

    def __init__(self, name: str,
                 height: float,
                 age: int,
                 growth: float):
        self._name = name
        self._height = height
        self._age_days = age
        self._growth = growth
        self._stats = self.Stats()

    def show(self) -> None:
        self._stats._count_show += 1
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

    @staticmethod
    def is_age(age: int) -> bool:
        if age > 365:
            return True
        return False

    @classmethod
    def unknow_plant(cls):
        return cls(name="Unknown plant", height=0.0, age=0, growth=0)


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
        print(f"[asking the {self._name.lower()} to grow and bloom]")
        self._bloomed = True
        super().grow(1)
        self._stats._count_grow += 1
        self.show()
        return


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._count_shade = 0

        def display(self) -> None:
            super().display()
            print(f" {self._count_shade} shade")

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
        self._stats._count_shade += 1
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
        self._stats._count_grow += 1
        self._stats._count_age += 1
        print(f"[make {self._name.lower()} grow and age for {days} days]")
        self._nutritional_value += days
        self.show()
        return


class Seed(Flower):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth: float,
                 color: str,
                 bloomed: bool = False,
                 seed: int = 0):
        super().__init__(name, height, age, growth, color, bloomed)
        self._seed = seed

    def show(self) -> None:
        super().show()
        if self._bloomed is False:
            print(" Seeds: 0")
        else:
            print(f" Seeds: {self._seed}")
        return

    def grow(self, days: int = 1) -> None:
        super().age(days)
        super().grow(days)
        self._stats._count_grow += 1
        self._stats._count_age += 1
        print(f"[make {self._name.lower()} grow, age and bloom]")
        self._bloomed = True
        self.show()


def show_plant_stats(plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_age(400)}")

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    rose.show()
    show_plant_stats(rose)
    rose.bloom()
    show_plant_stats(rose)

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 0.8, 5.0)
    oak.show()
    show_plant_stats(oak)
    oak.produce_shade()
    show_plant_stats(oak)

    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 1.5, "yellow", seed=42)
    sunflower.show()
    sunflower.grow(20)
    show_plant_stats(sunflower)

    print()
    print("=== Anonymous")
    unknown = Plant.unknow_plant()
    unknown.show()
    show_plant_stats(unknown)
