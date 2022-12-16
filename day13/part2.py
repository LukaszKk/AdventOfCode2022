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


def sort_packets(packets):
    n = len(packets)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            order = is_ordered(packets[j], packets[j+1])
            if order == -1:
                packets[j], packets[j + 1] = packets[j + 1], packets[j]


def calculate(lines):
    first_index = [[2]]
    second_index = [[6]]
    packets = [first_index, second_index]
    for left, right in get_pair(lines):
        packets.append(left)
        packets.append(right)

    sort_packets(packets)

    output = 1
    for index, packet in enumerate(packets):
        if packet == first_index or packet == second_index:
            output *= index + 1

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
