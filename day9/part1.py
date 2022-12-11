import os


class Board:
    def __init__(self):
        self.visited = []
        self.head = (0, 0)
        self.tail = (0, 0)
        self.mark_visited()

    def move(self, x, y):
        self.move_head(x, y)
        if self.tail_touches_head():
            return
        if self.move_if_on_track():
            return
        self.move_diagonally()
        self.mark_visited()

    def move_head(self, x, y):
        self.head = (x, y)

    def move_tail(self, x, y):
        self.tail = (x, y)

    def move_if_on_track(self):
        if self.head[0] == self.tail[0]:
            self.move_y_two_steps_away()
        elif self.head[1] == self.tail[1]:
            self.move_x_two_steps_away()

    def move_diagonally(self):
        if (self.head[0] == self.tail[0] + 1) or (self.head[0] == self.tail[0] - 1):
            self.move_y_two_steps_away()
        elif (self.head[1] == self.tail[1] + 1) or (self.head[1] == self.tail[1] - 1):
            self.move_x_two_steps_away()

    def move_y_two_steps_away(self):
        if self.head[1] == self.tail[1] + 2:
            self.move_tail(self.head[0], self.tail[1] + 1)
        elif self.head[1] == self.tail[1] - 2:
            self.move_tail(self.head[0], self.tail[1] - 1)

    def move_x_two_steps_away(self):
        if self.head[0] == self.tail[0] + 2:
            self.move_tail(self.tail[0] + 1, self.head[1])
        elif self.head[0] == self.tail[0] - 2:
            self.move_tail(self.tail[0] - 1, self.head[1])

    def tail_touches_head(self):
        if self.head[0] == self.tail[0]:
            if self.head[1] == self.tail[1]:
                return True
            if self.head[1] == self.tail[1] + 1:
                return True
            if self.head[1] == self.tail[1] - 1:
                return True
        elif self.head[1] == self.tail[1]:
            if self.head[0] == self.tail[0] + 1:
                return True
            if self.head[0] == self.tail[0] - 1:
                return True
        elif self.head[0] == self.tail[0] + 1:
            if self.head[1] == self.tail[1] + 1:
                return True
            elif self.head[1] == self.tail[1] - 1:
                return True
        elif self.head[0] == self.tail[0] - 1:
            if self.head[1] == self.tail[1] + 1:
                return True
            elif self.head[1] == self.tail[1] - 1:
                return True

    def mark_visited(self):
        if self.tail not in self.visited:
            self.visited.append(self.tail)


def calculate(lines):
    board = Board()
    for line in lines:
        values = line.strip().replace("\n", "").split(" ")
        for count in range(0, int(values[1])):
            if values[0] == "R":
                board.move(board.head[0] + 1, board.head[1])
            elif values[0] == "L":
                board.move(board.head[0] - 1, board.head[1])
            elif values[0] == "U":
                board.move(board.head[0], board.head[1] + 1)
            elif values[0] == "D":
                board.move(board.head[0], board.head[1] - 1)

    return len(board.visited)


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
