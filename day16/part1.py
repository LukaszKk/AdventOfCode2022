import os
import re


class Valve:
    def __init__(self, flow=0, neighbours=None):
        if neighbours is None:
            neighbours = []
        self.flow_rate = flow
        self.neighbours = neighbours

    def get_highest_neighbour(self):
        pass


class Valves:
    def __init__(self):
        self.valves = []

    @staticmethod
    def read(lines):
        valves = Valves()
        for line in lines:
            line_vals = line.strip().replace("\n", "").split(";")
            flow = int(re.search(r"\d+", line_vals[0]).group())
            neighbours = [x.strip() for x in re.split(r"valve.", line_vals[1])[1].split(",")]

            valve = Valve(flow, neighbours)
            valves.valves.append(valve)
        return valves


def calculate(lines):
    valves = Valves.read(lines)
    print(valves.valves[0].neighbours)
    return 0


def read_input():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir + "/input2.txt", "r") as f:
        return f.readlines()


def main():
    lines = read_input()
    output = calculate(lines)
    print(output)


if __name__ == "__main__":
    main()
