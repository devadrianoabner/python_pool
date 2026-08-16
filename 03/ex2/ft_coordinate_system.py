#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        print("Enter new coordinates as floats in format 'x,y,z': ",
              end="")
        new_input = input()
        splited_input = new_input.split(",")
        if len(splited_input) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(splited_input[0].strip())
            y = float(splited_input[1].strip())
            z = float(splited_input[2].strip())
        except ValueError as e:
            print(f"Error on parameter 'abc': {e}")
            continue
        return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    fisrt_dist = get_player_pos()
    print("Got a first tuple:", fisrt_dist)
    print(f"It includes: X={fisrt_dist[0]}, Y={fisrt_dist[1]},",
          f"Z={fisrt_dist[2]}")
    dist_center = math.sqrt(fisrt_dist[0] ** 2
                            + fisrt_dist[1] ** 2 + fisrt_dist[2] ** 2)
    print(f"Distance to center : {round(dist_center, 4)}")
    print()

    print("Get a second set of coordinates")
    second_dist = get_player_pos()
    dist = math.sqrt((second_dist[0] - fisrt_dist[0]) ** 2
                     + (second_dist[1] - fisrt_dist[1]) ** 2
                     + (second_dist[2] - fisrt_dist[2] ** 2))
    print("Distance between the 2 sets of coordinates: ", end="")
    print(f"{round(dist, 4)}")
