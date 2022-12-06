

if __name__ == '__main__':
    file = open('input.txt', 'r')
    Lines = file.readlines()
    line = Lines[0]
    line.strip()

    prev_chars = []
    marker_length = 14

    for i in range(len(line)):
        print(prev_chars)
        if len(set(prev_chars)) == marker_length:
            print(i)
            break

        if len(prev_chars) == marker_length:
            prev_chars.pop(0)

        prev_chars.append(line[i])
