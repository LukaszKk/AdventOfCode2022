import os
import operator
from functools import reduce


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}


class Animals:
    def __init__(self):
        self.monkeys = []

    def read_monkeys(self, lines):
        monkey_num = -1
        items = []
        monkey_operator = None
        monkey_value = -1
        value_to_test = None
        true_test = -1
        false_test = -1
        
        for line in lines:
            if not line.strip():
                monkey = Monkey(monkey_num, items)\
                    .build_operation(monkey_operator, monkey_value)\
                    .build_test(value_to_test, true_test, false_test)
                self.monkeys.append(monkey)
                continue

            values = line.strip().replace("\n", "").split(":")
            key = values[0]
            value = values[1]
            if "Monkey" in key:
                monkey_num = int(key.split(" ")[1])
            elif "Starting items" == key:
                items = [int(x.strip()) for x in value.split(", ")]
            elif "Operation" == key:
                monkey_operator = value.strip().split(" ")[3]
                monkey_value = value.strip().split(" ")[4]
            elif "Test" == key:
                value_to_test = int(value.strip().split(" ")[2])
            elif "If true" == key:
                true_test = int(value.strip().split(" ")[3])
            elif "If false" == key:
                false_test = int(value.strip().split(" ")[3])

        return self


class Monkey:
    def __init__(self, number: int, items: []):
        self.number = number
        self.items = items
        self._monkey_operator = "+"
        self._monkey_value = 0
        self.value_to_test = 1
        self.true_test = -1
        self.false_test = -1
        self.inspected = 0

    def build_operation(self, monkey_operator, monkey_value):
        self._monkey_operator = monkey_operator
        self._monkey_value = monkey_value
        return self

    def build_test(self, value_to_test, true_test, false_test):
        self.value_to_test = value_to_test
        self.true_test = true_test
        self.false_test = false_test
        return self

    def operation(self, value):
        monkey_value = value if "old" == self._monkey_value else int(self._monkey_value)
        return ops[self._monkey_operator](value, monkey_value)

    def test(self, value: int):
        return self.true_test if value % self.value_to_test == 0 else self.false_test

    def inspect(self, item_index):
        self.items[item_index] = self.operation(self.items[item_index])
        self.inspected += 1

    def decrease_worry_level(self, item_index):
        self.items[item_index] = int(self.items[item_index] / 3)

class Game:
    def __init__(self, animals):
        self.animals = animals

    def play(self):
        for round_index in range(0, 20):
            self.move_monkeys_items()

    def move_monkeys_items(self):
        for monkey in self.animals.monkeys:
            remove_items_indices = []
            for item_index in range(0, len(monkey.items)):
                monkey.inspect(item_index)
                monkey.decrease_worry_level(item_index)

                remove_items_indices.append(item_index)
                self.throw(monkey.test(monkey.items[item_index]), monkey.items[item_index])
            monkey.items = [item for index, item in enumerate(monkey.items) if index not in remove_items_indices]

    def throw(self, to, item):
        self.animals.monkeys[to].items.append(item)


def calculate(lines):
    animals = Animals().read_monkeys(lines)
    game = Game(animals)
    game.play()
    return reduce(lambda x, y: x * y, sorted([x.inspected for x in animals.monkeys], reverse=True)[0:2])


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
