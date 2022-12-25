import os
import re


def read_values(lines):
    beacons = list()
    sensors = list()
    for line in lines:
        line = line.strip().replace("\n", "")
        values = list(map(int, re.findall(r'-?\d+', line)))
        sensors.append((values[0], values[1]))
        beacons.append((values[2], values[3]))
    return beacons, sensors


def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))


def find_all_points_within_distance(taken_points, point, distance, value):
    for y in range(point[1], point[1] + distance + 1):
        if y == value:
            for x in range(0, distance + 1 - (y - point[1])):
                taken_points.add((point[0] + x, y))
                taken_points.add((point[0] - x, y))

    for y in range(point[1] - distance, point[1]):
        if y == value:
            for x in range(0, y - (point[1] - distance) + 1):
                taken_points.add((point[0] + x, y))
                taken_points.add((point[0] - x, y))

    return taken_points


def print_values(beacons, sensors, points):
    for y in range(-2, 23):
        for x in range(-3, 26):
            if x == -3:
                end = " " if y < 0 or y >= 10 else "  "
                print(y, end=end)
            elif (x, y) in beacons:
                print("B", end="")
            elif (x, y) in sensors:
                print("S", end="")
            elif (x, y) in points:
                print("#", end="")
            else:
                print(".", end="")
        print()


def calculate(lines):
    beacons, sensors = read_values(lines)
    taken_points = set()
    value = 2000000
    for sensor, beacon in zip(sensors, beacons):
        distance = manhattan_distance(sensor, beacon)
        find_all_points_within_distance(taken_points, sensor, distance, value)

    # print_values(beacons, sensors, taken_points)

    taken_points = [point for point in taken_points if point not in beacons and point not in sensors]
    return len(taken_points)


def read_input():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir + "/input.txt", "r") as f:
        return f.readlines()


def main():
    lines = read_input()
    output = calculate(lines)
    print(output)


if __name__ == "__main__":
    main()
