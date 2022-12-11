import os


def build_map(lines):
    tree_map = []
    for line in lines:
        tree_map.append(list(map(int, line.strip().replace("\n", ""))))
    return tree_map


def calculate(lines):
    outputs = []
    tree_map = build_map(lines)
    for y in range(1, len(tree_map) - 1):
        for x in range(1, len(tree_map[0]) - 1):
            current_tree = tree_map[y][x]

            count = 0
            found_bigger = False
            for xx in range(x - 1, -1, -1):
                count += 1
                if tree_map[y][xx] >= current_tree:
                    outputs.append(count)
                    found_bigger = True
                    break
            if not found_bigger:
                outputs.append(count)

            count = 0
            found_bigger = False
            for xx in range(x + 1, len(tree_map[0])):
                count += 1
                if tree_map[y][xx] >= current_tree:
                    outputs[len(outputs) - 1] = outputs[len(outputs) - 1] * count
                    found_bigger = True
                    break
            if not found_bigger:
                outputs[len(outputs) - 1] = outputs[len(outputs) - 1] * count

            count = 0
            found_bigger = False
            for yy in range(y - 1, -1, -1):
                count += 1
                if tree_map[yy][x] >= current_tree:
                    outputs[len(outputs) - 1] = outputs[len(outputs) - 1] * count
                    found_bigger = True
                    break
            if not found_bigger:
                outputs[len(outputs) - 1] = outputs[len(outputs) - 1] * count

            count = 0
            found_bigger = False
            for yy in range(y + 1, len(tree_map)):
                count += 1
                if tree_map[yy][x] >= current_tree:
                    outputs[len(outputs) - 1] = outputs[len(outputs) - 1] * count
                    found_bigger = True
                    break
            if not found_bigger:
                outputs[len(outputs) - 1] = outputs[len(outputs) - 1] * count

    return max(outputs)

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
