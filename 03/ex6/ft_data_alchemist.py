#!/usr/bin/env python3
import random


PLAYERS = ["Alice", "bob", "Charlie", "dylan", "Emma",
           "Gregory", "john", "kevin", "Liam"]


def capitalize_all(players: list[str]) -> list[str]:
    return [name.capitalize() for name in players]


def filter_capitalized(players: list[str]) -> list[str]:
    return [name for name in players if name == name.capitalize()]


def build_score_dict(names: list[str]) -> dict[str, int]:
    return {name: random.randint(1, 999) for name in names}


def compute_average(scores: dict[str, int], names: list[str]) -> float:
    values = [scores[name] for name in names]
    return sum(values) / len(values)


def filter_high_scores(
    scores: dict[str, int], names: list[str], average: float
) -> dict[str, int]:
    return {
        name: scores[name] for name in names if scores[name] > average
    }


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()

    print("Initial list of players:", PLAYERS)
    capitalized = capitalize_all(PLAYERS)
    print("New list with all names capitalized:", capitalized)

    only_capitalized = filter_capitalized(PLAYERS)
    print("New list of capitalized names only:", only_capitalized)
    print()

    scores = build_score_dict(capitalized)
    print("Score dict:", scores)

    average = compute_average(scores, capitalized)
    print(f"Score average is {round(average, 2)}")

    high_scores = filter_high_scores(scores, capitalized, average)
    print("High scores:", high_scores)
