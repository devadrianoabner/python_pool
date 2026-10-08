#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str = "Unknown Animal",
                 sound: str = "Unknown Sound",
                 age: int = 0) -> None:
        self._name = name
        self._sound = sound
        self.age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            print("Animals with negative age do not exist",
                  "default value added",
                  f"{self._name} age = 0", sep="\n")
            self._age = 0
        else:
            self._age = value

    @abstractmethod
    def animal_sound(self) -> None:
        print(f"The {self._name} goes {self._sound}")

    def animal_info(self) -> None:
        print(f"This is the information about this {self._name}")


class Dog(Animal):
    def __init__(self,
                 energy: int = 10,
                 name: str = "Unknown Dog",
                 sound: str = "Au! Au!",
                 age: int = 0) -> None:
        super().__init__(name, sound, age)
        self.energy = energy

    @property
    def energy(self) -> int:
        return self._energy

    @energy.setter
    def energy(self, value: int) -> None:
        if value < 0:
            print("Animals with negative energy do not exist",
                  "default value added",
                  f"{self._name} energy = 10", sep='\n')
            self._energy = 10
        else:
            self._energy = value

    @property
    def human_age(self) -> int:
        if self.age == 0:
            print(f"The {self._name}",
                  "has not yet reached the minimum human age")
            return 0
        else:
            return self.age * 7

#    def animal_sound(self) -> None:
#        super().animal_sound()

    def dig(self) -> None:
        if self._energy > 0:
            self._energy -= 1
        else:
            print(f"The {self._name} is tired")

    def __str__(self) -> str:
        return (
            f"Dog name: {self._name}, "
            f"Age: {self.age}, "
            f"Energy: {self.energy}"
        )

    def dog_info(self) -> None:
        super().animal_info()
        print(self)


if __name__ == "__main__":
    Dog().animal_sound()
