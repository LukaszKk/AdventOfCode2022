import os
import re


def read_values(lines):
    beacons = set()
    sensors = set()
    for line in lines:
        line = line.strip().replace("\n", "")
        values = list(map(int, re.findall(r'-?\d+', line)))
        sensors.add((values[0], values[1]))
        beacons.add((values[2], values[3]))
    return beacons, sensors


def print_values(beacons, sensors):
    for y in range(0, 23):
        for x in range(-3, 26):
            if x == -3:
                end = "  " if y < 10 else " "
                print(y, end=end)
            elif (x, y) in beacons:
                print("B", end="")
            elif (x, y) in sensors:
                print("S", end="")
            else:
                print(".", end="")
        print()


def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))


def calculate(lines):
    beacons, sensors = read_values(lines)
    distance = manhattan_distance((8, 7), (2, 10))
    print_values(beacons, sensors)
    return distance


def read_input():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir + "/input2.txt", "r") as f:
        return f.readlines()


def main():
    lines = read_input()
    output = calculate(lines)
    print(output)


if __name__ == "__main__":
    main()
