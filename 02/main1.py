
sums = []

if __name__ == '__main__':
    inputFile = open('input.txt', 'r')
    Lines = inputFile.readlines()

    for line in Lines:
        he = ord(line[0]) - ord("A")
        me = ord(line[2]) - ord("X")

        if me == he:
            points = 3
        elif (me == 0 and he == 2) or (me == he + 1):
            points = 6
        else:
            points = 0

        points += me + 1

        sums.append(points)

    # for s in sums:
    #     print(s)

    print(sum(sums))
