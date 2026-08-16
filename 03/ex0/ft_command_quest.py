#!/usr/bin/env python3
import sys


def print_args() -> None:
    print("=== Command Quest ===")
    total_args = 0
    args = sys.argv[1:]
    for _ in args:
        total_args += 1
    print(f"Arguments received: {total_args}")
    num = 1
    for i in args:
        print(f"Argument {num }: {i}")
        num += 1
    print(f"Total arguments: {total_args + 1}\n")


if __name__ == "__main__":
    print_args()
