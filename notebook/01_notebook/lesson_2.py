

class Tool:
    class Stats:
        def __init__(self, use_count: int = 0):
            self._use_count = use_count

    def __init__(self,
                 name: str,
                 capacity: int,
                 composition: str):
        self._name = name
        self._capacity = capacity
        self._composition = composition
        self._status = self.Stats()

    def show(self) -> None:
        print(self._name, self._capacity,
              self._composition, self._status._use_count)

    def get_capacity(self) -> int:
        return self._capacity

    def set_capacity(self, amount: int) -> None:
        if amount < 0:
            print("Enter only positive values.")
            return
        self._capacity = amount

    def set_composition(self, material: str) -> None:
        if material not in ["Metal", "Plastic", "Titanium", "Wood"]:
            print("Non-existent material")
            return
        self._composition = material

    def use(self, amount: int = 1) -> None:
        if self._capacity == 0:
            print("empty")
            return
        if self._capacity < amount:
            overflow = amount - self._capacity
            print("Use:", amount)
            print("Capacity overflow")
            print(f"Overflow of {overflow}")
            self.set_capacity(0)
            print("Current capacity:", self._capacity)
            return
        self._capacity -= amount
        print(self._capacity)

    def set_use_count(self, use: int = 0):
        if use < 0:
            print("Enter only positive values.")
            return
        self._use_count = use

    @classmethod
    def make_tools(cls):
        return cls(name="Sprinkler", capacity=20, composition="Metal")

    @staticmethod
    def is_valid_capacity(amount: int) -> bool:
        if amount > 0 and amount < 100:
            return True
        return False


class PowerTool(Tool):
    def __init__(self,
                 name: str,
                 capacity: int,
                 composition: str,
                 voltage: int):
        super().__init__(name, capacity, composition)
        self._voltage = voltage

    def show(self) -> None:
        super().show()
        print(f"Voltage: {self._voltage}")

    def turn_on(self) -> None:
        print(self._name, f"It's running on {self._voltage} volts")


def print_tool():
    sprinkler = Tool("Sprinkler", 5, "Plastic")
    sprinkler.show()
    sprinkler.set_composition("Metal")
    sprinkler.show()
    sprinkler.use(10)
    mega_sprinkler = PowerTool("Mega Sprinkle", 20, "Metal", 110)
    mega_sprinkler.show()
    mega_sprinkler.turn_on()
    sprinkler.set_use_count(3)
    new_tool = Tool.make_tools()
    new_tool.show()
    print(Tool.is_valid_capacity(50))
    print(Tool.is_valid_capacity(150))


print_tool()
