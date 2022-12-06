from collections import deque


class Ship:
    load = []
    for i in range(9):
        stack = deque()
        load.append(stack)

    def read_containers(self):
        for line in Lines:
            line.strip()

            if line[0] == ' ':
                break

            for stack in range(0, 9, 1):
                if line[1+4*stack] != ' ':
                    self.load[stack].appendleft(line[1+4*stack])
        # print(self.load)

    def add_to_top(self, y, containers):
        if task == 2:
            containers.reverse()

        for container in containers:
            self.load[y].append(container)

    def remove_from_top(self, x, nr):
        containers = []
        for container in range(0, nr, 1):
            containers.append(self.load[x][len(self.load[x])-1])
            self.load[x].pop()
        return containers

    def move(self):
        for line in Lines:
            if line[0] == 'm':
                line.strip()
                words = line.split()

                x = int(words[3]) - 1
                y = int(words[5]) - 1
                nr = int(words[1])

                self.add_to_top(y, self.remove_from_top(x, nr))
                # print(self.load)

    def print_top(self):
        print("Top Containers: ")
        for stack in self.load:
            print(stack[len(stack)-1], end="")


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    ship = Ship()
    task = 1

    ship.read_containers()
    ship.move()
    ship.print_top()

