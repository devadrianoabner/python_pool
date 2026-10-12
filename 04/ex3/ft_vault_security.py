#!/usr/bin/env python3


def secure_archive(
    filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename) as file:
                data = file.read()
            return (True, data)
        if action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
    except OSError as e:
        return (False, str(e))
    return (False, f"Unknown action: '{action}'")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file")
    print(result)
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/master.passwd")
    print(result)
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    result = secure_archive("new_vault.txt", "write", "some content")
    print(result)
