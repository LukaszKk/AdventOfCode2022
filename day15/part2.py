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


def find_border(point, distance, length):
    border_points = set()
    for y in range(point[1], point[1] + distance + 1):
        if 0 < y <= length:
            x = distance + 1 - (y - point[1])
            if 0 < point[0] + x <= length:
                border_points.add((point[0] + x, y))
            if 0 < point[0] - x <= length:
                border_points.add((point[0] - x, y))

    for y in range(point[1] - distance, point[1]):
        if 0 < y <= length:
            x = y - (point[1] - distance) + 1
            if 0 < point[0] + x <= length:
                border_points.add((point[0] + x, y))
            if 0 < point[0] - x <= length:
                border_points.add((point[0] - x, y))

    return border_points


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
    length = 4000000
    for sensor, beacon in zip(sensors, beacons):
        distance = manhattan_distance(sensor, beacon)
        border_points = find_border(sensor, distance, length)

        for border in border_points:
            inside = False

            for new_sensor, new_beacon in zip(sensors, beacons):
                new_distance = manhattan_distance(new_sensor, new_beacon)
                border_to_sensor_distance = manhattan_distance(new_sensor, border)
                if border_to_sensor_distance <= new_distance:
                    inside = True
                    break

            if not inside:
                print(border)
                return border[0] * 4000000 + border[1]

    return 0


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
