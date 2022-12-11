import os


class Directory:
    def __init__(self, current_name, parent):
        self.directories = []
        self.files_size = []
        self.parent = parent
        self.current_name = current_name

    def files_size_sum(self):
        return sum(self.files_size)

    def size(self):
        size = self.files_size_sum()
        for directory in self.directories:
            size += directory.size()
        return size


def read_directories(lines):
    current_directory = Directory(None, None)
    for line in lines:
        values = line.strip().replace("\n", "").split(" ")
        if values[0] == "$":
            if values[1] == "cd":
                if values[2] == "..":
                    current_directory = current_directory.parent
                    continue
                new_dir = Directory(values[2], current_directory)
                current_directory.directories.append(new_dir)
                current_directory = new_dir
        elif values[0] == "dir":
            continue
        else:
            current_directory.files_size.append(int(values[0]))

    return current_directory


def append_subdir_size(current_dir, size_list):
    for index in range(0, len(current_dir.directories)):
        directory = current_dir.directories[index]
        cur_size = directory.size()
        size_list.append(cur_size)
        append_subdir_size(directory, size_list)


def calculate(lines):
    output = 0
    current_dir = read_directories(lines)
    while current_dir.current_name != "/":
        current_dir = current_dir.parent

    current_size = current_dir.size()
    current_free_space = 70000000 - current_size
    size_list = [current_size]
    append_subdir_size(current_dir, size_list)
    current_size_to_free = 30000000 - current_free_space
    size_list = [x for x in size_list if x > current_size_to_free]
    output = min(size_list)

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
