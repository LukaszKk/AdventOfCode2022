import os


def calculate(lines):
    output = 0
    for line in lines:
        groups = line.split(",")
        first_group = groups[0].split("-")
        second_group = groups[1].split("-")
        first_group_values = set(range(int(first_group[0]), int(first_group[1])+1))
        second_group_values = set(range(int(second_group[0]), int(second_group[1])+1))
        if first_group_values.issubset(second_group_values) or second_group_values.issubset(first_group_values):
            output += 1

    return output


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
