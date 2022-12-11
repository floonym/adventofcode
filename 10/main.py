
class CPU:
    def __init__(self):
        self.x = [1, 1]

    def add_x(self, value):
        self.x.append(self.x[-1])
        self.x.append(self.x[-2] + value)

    def noop(self):
        self.x.append(self.x[-1])

    def read_command(self, text):
        words = text.split()
        if words[0] == 'noop':
            self.noop()
        if words[0] == 'addx':
            self.add_x(int(words[1]))

    def signal_strength(self):
        total = 0
        for i in range(20, len(self.x), 40):
            total += self.x[i] * i
            print(str(i) + "  " + str(self.x[i]) + "  " + str(self.x[i] * i))
        print(self.x)
        print(total)
        return total

    def check_pixel(self, cycle):
        position = cycle % 40 - 1
        if abs(position - self.x[cycle]) <= 1:
            print("#", end='')
            return True
        print(".", end='')
        return False

    def display(self):
        for y in range(1, 240):
            if y % 40 == 1:
                print()
            self.check_pixel(y)


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()

    cpu = CPU()

    for line in Lines:
        line = line.strip()
        cpu.read_command(line)

    cpu.signal_strength()

    cpu.display()




