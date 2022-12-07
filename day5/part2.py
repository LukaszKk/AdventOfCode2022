import os


def build_stack_struct(stacks):
    indexes = [x.replace("\n", "") for x in stacks[8:9]][0]
    stacks = [x.replace("\n", "") for x in stacks[0:8]]
    stack_struct = []
    for index, number in enumerate(indexes):
        if not number.isnumeric():
            continue
        stack_struct.append([])
        for stack in stacks:
            if len(stack) > index:
                value = stack[index]
                if value.isalpha():
                    stack_struct[int(number) - 1].insert(0, value)

    return stack_struct


def make_moves(stack_struct, moves):
    for move in moves:
        operators = [int(s) for s in move.split() if s.isdigit()]
        stack = stack_struct[operators[1] - 1]
        moved_value = stack[-operators[0]:]
        del stack[-operators[0]:]
        stack_struct[operators[2] - 1].extend(moved_value)
    return stack_struct


def calculate(lines):
    stack_struct = build_stack_struct(lines[0:9])
    output_stack_struct = make_moves(stack_struct, lines[10:])
    output = ""
    for stack in output_stack_struct:
        output += stack.pop()

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
