import os


def calculate(line):
    marker = line[0:14]
    for index in range(1, len(line)):
        if len(set(marker)) == 14:
            return marker, index + 1 + 12
        marker = line[index: index + 14]


def read_input():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir + "/input.txt", "r") as f:
        return f.readlines()


def main():
    lines = read_input()
    marker, output = calculate(lines[0])
    print(marker)
    print(output)


if __name__ == "__main__":
    main()
