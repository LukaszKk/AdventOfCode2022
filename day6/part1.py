import os


def calculate(line):
    marker = line[0:4]
    for index in range(1, len(line)):
        if len(set(marker)) == 4:
            return marker, index + 1 + 2
        marker = line[index: index + 4]


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
