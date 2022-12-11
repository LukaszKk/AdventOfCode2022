import os


class Cycles(object):
    def __init__(self):
        self._cycle = 0
        self._observers = []

    @property
    def cycle(self):
        return self._cycle

    @cycle.setter
    def cycle(self, value):
        self._cycle = value
        for callback in self._observers:
            callback(self._cycle)

    def bind_to(self, callback):
        self._observers.append(callback)


class CycleCal(object):
    def __init__(self, cpu):
        self.sum_strength = 0
        self.x = 1
        self.line_count = 0
        self.cpu = cpu
        self.cpu.bind_to(self.update_cycle_sum)
        self.cpu.bind_to(self.draw_crt)

    def update_cycle_sum(self, cycle):
        if (cycle - 20) % 40 == 0:
            self.sum_strength += self.x * cycle

    def draw_crt(self, cycle):
        sprite = cycle - self.line_count * 40 - 1
        if (sprite == self.x - 1) or (sprite == self.x) or (sprite == self.x + 1):
            print("#", end="")
        else:
            print(".", end="")
        if cycle % 40 == 0:
            print()
            self.line_count += 1



def calculate(lines):
    cpu = Cycles()
    cpu_strength = CycleCal(cpu)
    for line in lines:
        values = line.strip().replace("\n", "").split(" ")
        if values[0] == "noop":
            cpu.cycle += 1
        if values[0] == "addx":
            cpu.cycle += 1
            cpu.cycle += 1
            cpu_strength.x += int(values[1])
    return cpu_strength.sum_strength


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
