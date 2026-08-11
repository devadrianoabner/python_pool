

def drill_one():
    first_word = input()
    second_word = input()
    print(first_word, second_word, sep="-", end="")
    print("END")


def drill_two():
    first_number = int(input())
    second_number = int(input())
    print(first_number + second_number)


def drill_three():
    input_number = int(input())
    if input_number > 50:
        print("High")
    elif input_number == 50:
        print("Mid")
    else:
        print("Low")


def drill_for():
    input_number = int(input())
    for i in range(1, input_number + 1):
        print(i)


def drill_five(current, limit):
    print(current, limit)
    if current < limit:
        current += 1
        drill_five(current, limit)


def drill_six(seed_type: str, quantity: int) -> None:
    print(seed_type.capitalize(), quantity)
    return None
