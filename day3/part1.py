import os


def calculate(lines):
    output = 0
    for rucksack in lines:
        rucksack = rucksack.strip()
        length = int(len(rucksack)/2)
        first = set(rucksack[:length])
        second = set(rucksack[length:])
        for value in first:
            if value in second:
                if value.isupper():
                    output += ord(value) - 64 + 26
                else:
                    output += ord(value) - 96

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
