
sums = []

if __name__ == '__main__':
    inputFile = open('input.txt', 'r')
    Lines = inputFile.readlines()

    for line in Lines:
        he = ord(line[0]) - ord("A")
        me = he + (ord(line[2]) - ord("Y"))

        if me > 2:
            me = 0
        elif me < 0:
            me = 2

        if me == he:
            points = 3
        elif (me == 0 and he == 2) or (me == he + 1):
            points = 6
        else:
            points = 0

        points += me + 1

        sums.append(points)

    print(sum(sums))
