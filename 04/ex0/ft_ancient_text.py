#!/usr/bin/env python3
import sys
import typing


def open_file(filename: str) -> typing.IO[str]:
    file = open(filename)
    return file


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        file = open_file(filename)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    content = file.read()
    file.close()
    print("---")
    print()
    print(content)
    print("---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
