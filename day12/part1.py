import os
import time
from collections import deque


def read_height_map(lines):
    return [list(line.strip().replace("\n", "")) for line in lines]


def index_2d(rlist, value):
    for i, element in enumerate(rlist):
        if value in element:
            return i, element.index(value)


def find_path(heightmap, start, end):
    visited = set()
    queue = deque()
    queue.append([start])
    max_down = len(heightmap)
    max_right = len(heightmap[0])

    while queue:
        path = queue.popleft()
        node = path[-1]

        for neighbour_move in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            neighbour_y = node[0] + neighbour_move[0]
            neighbour_x = node[1] + neighbour_move[1]
            neighbour = (neighbour_y, neighbour_x)

            if 0 <= neighbour_y < max_down and 0 <= neighbour_x < max_right:
                node_value = heightmap[node[0]][node[1]]
                neighbour_value = heightmap[neighbour_y][neighbour_x]
                height_difference = ord(neighbour_value) - ord(node_value)

                if (height_difference <= 1) and (neighbour not in visited):
                    visited.add(neighbour)

                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == end:
                        print("Found")
                        return new_path

    print("Didnt find")
    return -1


def calculate(lines):
    start_time = time.time()
    heightmap = read_height_map(lines)
    start = index_2d(heightmap, "S")
    end = index_2d(heightmap, "E")
    heightmap[start[0]][start[1]] = "`"
    heightmap[end[0]][end[1]] = "{"

    output = find_path(heightmap, start, end)
    end_time = time.time()
    print(f"All: {end_time - start_time}")
    return len(output) - 1


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
