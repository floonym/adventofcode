from collections import deque


class Directory:

    def __init__(self, name, size):
        self.name = name
        self.size = int(size)
        self.content = []
        self.cursor_own = False
        self.cursor_content = 0

    def check_content_cursor(self):
        for x in range(len(self.content)):
            # print(self.content[x].name)
            if self.content[x].cursor_own:
                self.cursor_content = x
                return True
        return False

    def navigate(self, command):
        # print(self.check_content_cursor())
        if not self.cursor_own:
            return False
        if self.check_content_cursor():
            if self.content[self.cursor_content].navigate(command):
                return True
        return self.execute(command)

    def execute(self, command):  # return True if command was executed and parent doesn't have to do anything
        words = command.split()
        print("Where: " + self.name + "  What: " + command)
        if words[0] != '$':
            print("Create child in " + self.name + " : " + words[1])
            if words[0] == 'dir':
                self.content.append(Directory(words[1], 0))
            else:
                self.content.append(File(words[1], words[0]))
            return True

        if words[1] == 'cd':
            if words[2] == '/':
                if self.name != '/':
                    self.cursor_own = 0
                return False
            if words[2] == '..':
                if self.name != '/':
                    self.cursor_own = 0
                return True
            for sub in self.content:
                if words[2] == sub.name:
                    sub.cursor_own = True
                    print("Cursor set: " + sub.name + " " + str(sub.cursor_own))
                    return True
            print("Error, " + words[2] + " is not content of " + self.name + "  Cannot execute cd to directory")

        elif words[1] != 'ls':
            print("Unknown Command " + str(words))

        return True

    def calc_size(self):
        self.size = 0
        for sub in self.content:
            self.size += sub.calc_size()
        return self.size

    def size_below(self, limit):
        x = 0
        for sub in self.content:
            x += sub.size_below(limit)
        if self.size <= limit:
            x += self.size
        return x

    def task2(self, minimum):
        smallest = 100000000
        for sub in self.content:
            if sub.task2(minim) < smallest:
                smallest = sub.task2(minim)
        if minimum < self.size < smallest:
            smallest = self.size

        return smallest


class File(Directory):

    def calc_size(self):
        return self.size

    def size_below(self, limit):
        return 0

    def navigate(self, command):
        return False

    def check_content_cursor(self):
        return False


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()

    root = Directory('/', 0)
    root.cursor_own = True

    for line in Lines:
        line.strip()
        print("Line: " + line)
        root.navigate(line)
        print('\n')

    root.calc_size()
    print("Sum of folders below 100000: " + str(root.size_below(100000)))

    minim = root.size + 30000000 - 70000000
    print("Minimum to be deleted: " + str(minim))
    print("Size of smallest Folder zo delete: " + str(root.task2(minim)))



