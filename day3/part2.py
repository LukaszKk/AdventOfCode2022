import os


def calculate(lines):
    output = 0
    group_iter = 1
    three_rucksacks_list = []
    for rucksack in lines:
        rucksack = list(set(rucksack.strip()))
        three_rucksacks_list.append(rucksack)
        group_iter = 1 if group_iter == 3 else group_iter + 1
        if group_iter == 1:
            three_rucksacks_list = flatten(three_rucksacks_list)
            badge = set([value for value in three_rucksacks_list if three_rucksacks_list.count(value) == 3])
            if len(badge) > 0:
                value = next(iter(badge))
                if value.isupper():
                    output += ord(value) - 64 + 26
                else:
                    output += ord(value) - 96
            three_rucksacks_list = []

    return output


def flatten(main_list):
    return [item for sublist in main_list for item in sublist]


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
