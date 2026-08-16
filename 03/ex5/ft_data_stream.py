#!/usr/bin/env python3
import random
import typing

PLAYERS = ["bob", "alice", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb",
           "swim", "release", "use"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
        events: list[tuple[str, str]]
 ) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randint(0, len(events) - 1)
        event = events[index]
        events[index:index + 1] = []
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    events_gen = gen_event()
    for i in range(1000):
        name, action = next(events_gen)
        print(f"Event {i}: Player {name} did action {action}")

    ten_events = [next(events_gen) for _ in range(10)]
    print("Built list of 10 events:", ten_events)

    for event in consume_event(ten_events):
        print("Got event from list:", event)
        print("Remains in list", ten_events)
