#!/usr/bin/env python3
import sys
import typing


def open_file(filename: str) -> typing.IO[str]:
    file = open(filename)
    return file


def transform_content(content: str) -> str:
    lines = content.split("\n")
    new_lines = []
    for line in lines:
        if line != "":
            new_line = line + "#"
        else:
            new_line = line
        new_lines.append(new_line)
    new_content = "\n".join(new_lines)
    return new_content


def save_file(filename: str, content: str) -> None:
    file = open(filename, "w")
    file.write(content)
    file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        file = open_file(filename)
    except OSError as e:
        error_message = f"[STDERR] Error opening file '{filename}': {e}"
        print(error_message, file=sys.stderr)
        return
    content = file.read()
    file.close()
    print("---")
    print()
    print(content)
    print("---")
    print(f"File '{filename}' closed.")
    print()
    new_content = transform_content(content)
    print("Transform data:")
    print("---")
    print()
    print(new_content)
    print("---")
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_filename = sys.stdin.readline()
    new_filename = new_filename.strip()
    if new_filename == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_filename}'")
    try:
        save_file(new_filename, new_content)
    except OSError as e:
        error_message = f"[STDERR] Error opening file '{new_filename}': {e}"
        print(error_message, file=sys.stderr)
        print("Data not saved.")
        return
    print(f"Data saved in file '{new_filename}'.")


if __name__ == "__main__":
    main()
