import os


def build_map(lines):
    tree_map = []
    for line in lines:
        tree_map.append(list(map(int, line.strip().replace("\n", ""))))
    return tree_map


def calculate(lines):
    output = 0
    tree_map = build_map(lines)
    for y in range(1, len(tree_map) - 1):
        for x in range(1, len(tree_map[0]) - 1):
            current_tree = tree_map[y][x]

            bigger = True
            for xx in range(0, x):
                co = tree_map[y][xx]
                if co >= current_tree:
                    bigger = False
                    break
            if bigger:
                output += 1
                continue

            bigger = True
            for xx in range(x + 1, len(tree_map[0])):
                if tree_map[y][xx] >= current_tree:
                    bigger = False
                    break
            if bigger:
                output += 1
                continue

            bigger = True
            for yy in range(0, y):
                if tree_map[yy][x] >= current_tree:
                    bigger = False
                    break
            if bigger:
                output += 1
                continue

            bigger = True
            for yy in range(y + 1, len(tree_map)):
                if tree_map[yy][x] >= current_tree:
                    bigger = False
                    break
            if bigger:
                output += 1
                continue

    return output + len(tree_map) * 2 + len(tree_map[0]) * 2 - 4


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
