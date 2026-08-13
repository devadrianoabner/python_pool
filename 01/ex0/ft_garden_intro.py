#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str,
                 height: int,
                 age: int):
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"Plant: {self._name}",
              f"Height: {self._height}cm",
              f"Age: {self._age} days",
              sep="\n")


def new_plant():
    print("=== Welcome to My Garden ===")
    rose = Plant("Rose", 25, 30)
    rose.show()
    print("")
    print("=== End of Program ===")


if __name__ == "__main__":
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}", f"Height: {height}cm", f"Age: {age} days",
          sep="\n")
    print("")
    print("=== End of Program ===")
#    new_plant()
