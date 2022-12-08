from collections import deque


class Tree:

    def __init__(self, height, x, y):
        self.height = height
        self.visible = 0
        self.x = x
        self.y = y
        self.score = 0

    def check_view(self):
        x_negative = -1
        x_positive = -1
        y_negative = -1
        y_positive = -1
        not_visible_counter = 4
        for i in range(self.x - 1, -1, -1):
            x_negative = self.x - i
            if forrest[self.y][i].height >= self.height:
                not_visible_counter -= 1
                break
        for i in range(self.x + 1, len(forrest[self.y]), 1):
            x_positive = i - self.x
            if forrest[self.y][i].height >= self.height:
                not_visible_counter -= 1
                break
        for i in range(self.y - 1, -1, -1):
            y_negative = self.y - i
            if forrest[i][self.x].height >= self.height:
                not_visible_counter -= 1
                break
        for i in range(self.y + 1, len(forrest), 1):
            y_positive = i - self.y
            if forrest[i][self.x].height >= self.height:
                not_visible_counter -= 1
                break

        self.visible = bool(not_visible_counter)
        self.score = x_negative * x_positive * y_negative * y_positive


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()

    forrest = []

    for y in range(len(Lines)):
        line = Lines[y].strip()
        row = []
        for x in range(len(line)):
            row.append(Tree(int(line[x]), x, y))
        forrest.append(row)

    sum_visible = 0
    max_score = 0
    for row in forrest:
        for tree in row:
            tree.check_view()
            sum_visible += tree.visible
            max_score = max(tree.score, max_score)

    print(sum_visible)
    print(max_score)
