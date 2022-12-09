
class HeadTail:
    def __init__(self):
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
        self.log = {(0, 0)}

    def set_head(self, head):
        self.head_x, self.head_y = head

    def get_head(self):
        return self.head_x, self.head_y

    def get_tail(self):
        return self.tail_x, self.tail_y

    def move_head(self, direction):
        if direction == "U":
            self.head_x -= 1
        elif direction == "D":
            self.head_x += 1
        elif direction == "L":
            self.head_y -= 1
        elif direction == "R":
            self.head_y += 1
        print("Head: " + str(self.head_x) + " " + str(self.head_y))

    def tail_within9(self):
        if self.tail_x - 1 > self.head_x:
            return False
        if self.tail_x + 1 < self.head_x:
            return False
        if self.tail_y - 1 > self.head_y:
            return False
        if self.tail_y + 1 < self.head_y:
            return False
        print("true")
        return True

    def move_tail(self):
        if self.head_x < self.tail_x and self.head_y < self.tail_y:
            # Move the tail diagonally up and to the left
            self.tail_x -= 1
            self.tail_y -= 1
        elif self.head_x < self.tail_x and self.head_y > self.tail_y:
            # Move the tail diagonally up and to the right
            self.tail_x -= 1
            self.tail_y += 1
        elif self.head_x > self.tail_x and self.head_y < self.tail_y:
            # Move the tail diagonally down and to the left
            self.tail_x += 1
            self.tail_y -= 1
        elif self.head_x > self.tail_x and self.head_y > self.tail_y:
            # Move the tail diagonally down and to the right
            self.tail_x += 1
            self.tail_y += 1
        elif self.head_x < self.tail_x:
            self.tail_x -= 1
        elif self.head_x > self.tail_x:
            self.tail_x += 1
        elif self.head_y < self.tail_y:
            self.tail_y -= 1
        elif self.head_y > self.tail_y:
            self.tail_y += 1
        print("Tail: " + str(self.tail_x) + " " + str(self.tail_y))

    def log_tail(self):
        self.log.add((self.tail_x, self.tail_y))


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()

    snake = []
    for i in range(9):
        snake.append(HeadTail())

    for line in Lines:
        line = line.strip()
        words = line.split()
        for i in range(int(words[1])):
            snake[0].move_head(words[0])
            for k in range(len(snake)):
                if not snake[k].tail_within9():
                    snake[k].move_tail()
                    snake[k].log_tail()
                snake[min(k+1, len(snake)-1)].set_head(snake[k].get_tail())
            print()

    print(len(snake[0].log))
    print(len(snake[8].log))



