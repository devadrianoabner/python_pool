#!/usr/bin/env python3
import sys


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts = arg.split(":", 1)
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, quantity_str = parts
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for {name}: {e}")
            continue
        inventory[name] = quantity
    print("Got inventory:", inventory)

    items = list(inventory.keys())
    print("Item list:", items)
    if not items:
        return

    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    for name in items:
        quantity = inventory[name]
        percent = round(quantity / total * 100, 1)
        print(f"Item {name} represents {percent}%")

    most_name, most_quantity = items[0], inventory[items[0]]
    least_name, least_quantity = items[0], inventory[items[0]]
    for name in items:
        quantity = inventory[name]
        if quantity > most_quantity:
            most_name, most_quantity = name, quantity
        if quantity < least_quantity:
            least_name, least_quantity = name, quantity
    print(f"Item most abundant: {most_name} with quantity {most_quantity}")
    print(f"Item least abundant: {least_name} with quantity {least_quantity}")

    inventory.update({"magic:item": 1})
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    ft_inventory_system()
