#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    temps = ["25", "abc"]
    for temp_str in temps:
        try:
            print(f"Input data is '{temp_str}'")
            temp_int = input_temperature(temp_str)
            print(f"Temperature is now {temp_int}°C")
            print()
        except ValueError as e:
            print("Caught input_temperature error:", e)


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
