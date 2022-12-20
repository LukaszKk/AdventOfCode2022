import os


ROCK = "#"
AIR = "."
SAND_START = "+"
SAND = "O"


class Board:
    def __init__(self):
        self.rock_points = set()
        self.board = []
        self.min_x = 99999999
        self.max_x = -99999999
        self.min_y = 99999999
        self.max_y = -99999999
        self.sand_starting_position = (0, 500)
        self.rest = 0

    def read_pairs(self, pairs):
        previous_x = 0
        previous_y = 0
        for i, pair in enumerate(pairs):
            x, y = pair.split(",")
            x = int(x)
            y = int(y)

            self.min_x = x if x < self.min_x else self.min_x
            self.min_y = y if y < self.min_y else self.min_y
            self.max_x = x if x > self.max_x else self.max_x
            self.max_y = y if y > self.max_y else self.max_y

            if i == 0:
                self.rock_points.add((x, y))
            elif x == previous_x:
                lower = y if y < previous_y else previous_y
                higher = y if y > previous_y else previous_y
                for j in range(lower, higher + 1):
                    self.rock_points.add((x, j))
            elif y == previous_y:
                lower = x if x < previous_x else previous_x
                higher = x if x > previous_x else previous_x
                for j in range(lower, higher + 1):
                    self.rock_points.add((j, y))
            previous_x = x
            previous_y = y

    def fill(self):
        for y in range(0, self.max_y + 1):
            self.board.append([])
            for x in range(0, self.max_x + 1):
                if (y, x) == self.sand_starting_position:
                    self.board[y].append(SAND_START)
                elif (x, y) in self.rock_points:
                    self.board[y].append(ROCK)
                else:
                    self.board[y].append(AIR)

    def print(self):
        for y in range(0, self.max_y + 1):
            for x in range(self.min_x - 1, self.max_x + 1):
                print(self.board[y][x], end="")
            print()

    def fall_sand(self):
        position = self.sand_starting_position
        while True:
            if len(self.board) - 2 < position[0]:
                return

            if self.board[position[0] + 1][position[1]] == AIR:
                if position != self.sand_starting_position:
                    self.board[position[0]][position[1]] = AIR
                self.board[position[0] + 1][position[1]] = SAND
                position = (position[0] + 1, position[1])
            elif (position[1] - 1 > 0) and (self.board[position[0] + 1][position[1] - 1] == AIR):
                if position != self.sand_starting_position:
                    self.board[position[0]][position[1]] = AIR
                self.board[position[0] + 1][position[1] - 1] = SAND
                position = (position[0] + 1, position[1] - 1)
            elif (position[1] + 1 < len(self.board[position[0] + 1])) and (
                    self.board[position[0] + 1][position[1] + 1] == AIR):
                if position != self.sand_starting_position:
                    self.board[position[0]][position[1]] = AIR
                self.board[position[0] + 1][position[1] + 1] = SAND
                position = (position[0] + 1, position[1] + 1)
            else:
                self.rest += 1
                position = self.sand_starting_position

    @staticmethod
    def create(lines):
        board = Board()
        for line in lines:
            pairs = line.strip().replace("\n", "").split(" -> ")
            board.read_pairs(pairs)

        board.fill()
        return board


def calculate(lines):
    board = Board.create(lines)
    board.fall_sand()
    board.print()

    return board.rest


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
