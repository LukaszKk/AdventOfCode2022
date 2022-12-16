import os


def get_pair(lines):
    pair = ()
    for line in lines:
        packet = line.strip().replace("\n", "")
        if not packet:
            yield pair[0], pair[1]
            pair = ()
            continue
        pair = (*pair, eval(packet))


def compare(left_val, right_val):
    if left_val < right_val:
        return 1
    if left_val > right_val:
        return -1
    return 0


def verify_list(left_val, right_val):
    if type(left_val) is list and type(right_val) is list:
        return left_val, right_val
    if type(left_val) is list:
        return left_val, [right_val]
    return [left_val], right_val


def is_ordered(left, right):
    for left_val, right_val in zip(left, right):
        if type(left_val) is int and type(right_val) is int:
            ordered = compare(left_val, right_val)
        else:
            left_val, right_val = verify_list(left_val, right_val)
            ordered = is_ordered(left_val, right_val)

        if ordered == 0:
            continue
        return ordered

    if len(left) > len(right):
        return -1
    if len(left) < len(right):
        return 1
    return 0


def calculate(lines):
    output = 0
    index = 1
    for left, right in get_pair(lines):
        if is_ordered(left, right) == 1:
            output += index
        index += 1

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
