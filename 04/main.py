
class Assignment:
    lower = 0
    upper = 0

    def read(self, pair):
        self.lower = int(pair.split('-')[0])
        self.upper = int(pair.split('-')[1])
        # print(str(self.lower)+" "+str(self.upper))


class Elves:
    assi1 = Assignment()
    assi2 = Assignment()
    counter_inside = 0
    counter_overlap = 0
    def read(self, line):
        line = line.strip()
        text = line.split(',')
        print(text)
        self.assi1.read(text[0])
        self.assi2.read(text[1])

    def check_if_inside(self, ass):
        if ass[0].lower <= ass[1].lower:
            if ass[0].upper >= ass[1].upper:
                return True

    def check_if_inside_2way(self):
        if self.check_if_inside([self.assi1, self.assi2]):
            # print("2 in 1")
            self.counter_inside += 1
            return True
        elif self.check_if_inside([self.assi2, self.assi1]):
            # print("1 in 2")
            self.counter_inside += 1
            return True
        return False

    def check_overlap(self):
        if self.assi1.lower <= self.assi2.upper:
            if self.assi1.upper >= self.assi2.lower:
                print("Overlap")
                self.counter_overlap += 1
                return True


def task1():
    elves = Elves()
    for line in Lines:
        elves.read(line)
        elves.check_if_inside_2way()
        elves.check_overlap()

    print('Task 1: ' + str(elves.counter_inside))
    print('Task 2: ' + str(elves.counter_overlap))


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()

    task1()
