#!/usr/bin/env python3
import random


ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder"
    ]


def gen_player_achievements() -> set[str]:
    count = random.randint(4, 9)
    picked = random.sample(ACHIEVEMENTS, count)
    return set(picked)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    players = [
        ("Alice", alice), ("Bob", bob), ("Charlie", charlie), ("Dylan", dylan)
    ]
    for name, achievements in players:
        print(f"Player {name}: {achievements}")
    print()

    all_achievements = alice.union(bob, charlie, dylan)
    print("All distinct achievements:", all_achievements)
    print()

    common_achievements = alice.intersection(bob, charlie, dylan)
    print("Commom achievements:", common_achievements)
    print()

    alice_achieves = alice.difference(bob.union(charlie, dylan))
    bob_achieves = bob.difference(alice.union(charlie, dylan))
    charlie_achieves = charlie.difference(alice.union(bob, dylan))
    dylan_achieves = dylan.difference(alice.union(bob, charlie))
    print("Only Alice has:", alice_achieves)
    print("Only Bob has:", bob_achieves)
    print("Only Charlie has:", charlie_achieves)
    print("Only Dylan has:", dylan_achieves)
    print()

    print("Alice is missing:", all_achievements.difference(alice))
    print("Bob is missing:", all_achievements.difference(bob))
    print("Charlie is missing:", all_achievements.difference(charlie))
    print("Dylan is missing:", all_achievements.difference(dylan))
