#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str,
                 height: int,
                 age: int):
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}:",
              f"{self._height}cm,",
              f"{self._age} days old",)


def new_plant():
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sun_flower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.show()
    sun_flower.show()
    cactus.show()


if __name__ == "__main__":
    new_plant()
