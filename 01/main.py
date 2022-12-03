
current = 0
sums = []

if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()

    for line in Lines:
        if line.strip() != "":
            current += int(line)
        else:
            sums.append(current)
            current = 0

    sums.sort(reverse=True)

#   for s in sums:
#      print(s)

    print(sums[0])          # first task
    print(sum(sums[0:3]))   # second task
