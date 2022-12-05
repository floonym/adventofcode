
class Ship:
    stack_height = 100
    load = [[0 for i in range(100)] for j in range(9)]

    def read_containers(self):
        counter = 0

        for line in Lines:
            line.strip()

            if line[0] == ' ':
                break

            for stack in range(0, 9, 1):
                if line[1+4*stack] != ' ':
                    self.load[stack][counter+self.stack_height-8] = line[1+4*stack]
                    self.load[stack][0] += 1

            counter += 1

        print(self.load)

    def add_to_top(self, y, containers):
        if task == 2:
            containers.reverse()

        for container in containers:
            self.load[y][self.stack_height-1-self.load[y][0]] = container
            self.load[y][0] += 1

    def remove_from_top(self, x, nr):
        containers = []
        for container in range(0, nr, 1):
            containers.append(self.load[x][self.stack_height-self.load[x][0]])
            self.load[x][self.stack_height - self.load[x][0]] = 0
            self.load[x][0] -= 1
        return containers

    def move(self, x, y, nr):
        x -= 1
        y -= 1
        self.add_to_top(y, self.remove_from_top(x, nr))
        print(self.load)

    def parse(self):
        for line in Lines:
            if line[0] == 'm':
                line.strip()
                words = line.split()
                self.move(int(words[3]), int(words[5]), int(words[1]))

    def print_top(self):
        print("Top Containers: ")
        for stack in self.load:
            print(stack[self.stack_height-stack[0]], end="")


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    ship = Ship()
    task = 1

    ship.read_containers()
    ship.parse()
    ship.print_top()

