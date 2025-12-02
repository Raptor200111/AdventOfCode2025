def rotations(f):
    nz = 0
    initialPos = 50

    for line in f:
        num = int(line[1:]) % 100
        if (line[0] == 'R'):
            initialPos += num
        elif (line[0] == 'L'):
            initialPos -= num
        initialPos %= 100
        if (initialPos == 0):
            nz += 1

    return nz


f = open("input.txt") # result 1150
#f = open("test.txt") #result 3

print(rotations(f))
