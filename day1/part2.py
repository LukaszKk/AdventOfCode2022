import os


def calculate(calories):
    max_calories = []
    elf_calorie_sum = 0
    for calorie in calories:
        calorie = calorie.strip()
        if not calorie:
            max_calories.append(elf_calorie_sum)
            elf_calorie_sum = 0
        else:
            elf_calorie_sum += int(calorie)

    max_calories.sort(reverse=True)
    return sum(max_calories[:3])


def read_input():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir + "/input.txt", "r") as f:
        return f.readlines()


def main():
    calories = read_input()
    max_calories = calculate(calories)
    print(max_calories)


if __name__ == "__main__":
    main()
