import os


class Board:
    def __init__(self):
        self.positions = [Position(), Position(), Position(), Position(),
                          Position(), Position(), Position(), Position(),
                          Position()]


class Position:
    def __init__(self):
        self.visited = []
        self.head = (0, 0)
        self.tail = (0, 0)
        self.mark_visited()

    def move_tail(self):
        if self.tail_touches_head():
            return
        if self.move_if_on_track():
            return
        self.move_diagonally()
        self.mark_visited()

    def move_head(self, x, y):
        self.head = (x, y)

    def __move_tail(self, x, y):
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
        elif self.head[0] == self.tail[0] + 2:
            if self.head[1] == self.tail[1] + 2:
                self.__move_tail(self.tail[0] + 1, self.tail[1] + 1)
            elif self.head[1] == self.tail[1] - 2:
                self.__move_tail(self.tail[0] + 1, self.tail[1] - 1)
        elif self.head[0] == self.tail[0] - 2:
            if self.head[1] == self.tail[1] + 2:
                self.__move_tail(self.tail[0] - 1, self.tail[1] + 1)
            elif self.head[1] == self.tail[1] - 2:
                self.__move_tail(self.tail[0] - 1, self.tail[1] - 1)

    def move_y_two_steps_away(self):
        if self.head[1] == self.tail[1] + 2:
            self.__move_tail(self.head[0], self.tail[1] + 1)
        elif self.head[1] == self.tail[1] - 2:
            self.__move_tail(self.head[0], self.tail[1] - 1)

    def move_x_two_steps_away(self):
        if self.head[0] == self.tail[0] + 2:
            self.__move_tail(self.tail[0] + 1, self.head[1])
        elif self.head[0] == self.tail[0] - 2:
            self.__move_tail(self.tail[0] - 1, self.head[1])

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


def print_board(board):
    positions_list = [board.positions[0].head]
    print(board.positions[0].head)
    for position in board.positions:
        positions_list.append(position.tail)
        print(position.tail)

    for y in range(-18, 1):
        for x in range(-11, 1):
            if (x, y) in positions_list:
                print("*", end="")
            else:
                print(".", end="")
            print(" ", end="")
        print()


def calculate(lines):
    board = Board()
    for line in lines:
        values = line.strip().replace("\n", "").split(" ")
        for count in range(0, int(values[1])):
            head_position = board.positions[0]
            if values[0] == "R":
                head_position.move_head(head_position.head[0] + 1, head_position.head[1])
            elif values[0] == "L":
                head_position.move_head(head_position.head[0] - 1, head_position.head[1])
            elif values[0] == "U":
                head_position.move_head(head_position.head[0], head_position.head[1] - 1)
            elif values[0] == "D":
                head_position.move_head(head_position.head[0], head_position.head[1] + 1)

            for index in range(0, len(board.positions)):
                if index > 0:
                    board.positions[index].move_head(board.positions[index-1].tail[0], board.positions[index-1].tail[1])
                board.positions[index].move_tail()

    print_board(board)
    return len(board.positions[8].visited)


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
