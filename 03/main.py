

def priority(char):
    if ord(char) > ord("Z"):
        prio = ord(char) - 96
    else:
        prio = ord(char) - 64 + 26
    # print(char, end="  ")
    # print(prio)
    return prio


def task1():
    prios = []
    for line in Lines:
        line = line.strip()
        length = len(line)
        comp1 = line[0:int(length / 2)]
        comp2 = line[int(length / 2):int(length)]

        for char in comp1:
            if char in comp2:
                prios.append(priority(char))
                break

    print('Task 1: ' + str(sum(prios)))


def task2():
    prios = []
    for x in range(0, len(Lines), 3):
        for char in Lines[x].strip():
            if char in Lines[x+1] and char in Lines[x+2]:
                prios.append(priority(char))
                break

    print('Task 2: ' + str(sum(prios)))


if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()

    task1()
    task2()
