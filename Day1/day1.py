def rotationsPart1(f):
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

def rotationsPart2(f):
    nz = 0
    initialPos = 50

    for line in f:
        if (int(line[1:]) >= 100):
            nz += int(int(line[1:])/100)

        num = int(line[1:]) % 100

        if (line[0] == 'R'):
            initialPos += num
            if initialPos >= 100:
                nz += 1

        elif (line[0] == 'L'):
            if initialPos == 0:
                initialPos = num * -1
            else:
                initialPos -= num
                if initialPos <= 0:
                    nz += 1
        
        initialPos %= 100

    return nz


f = open("input.txt")
#f = open("test.txt")

#print(rotationsPart1(f)) #result test: 3, input: 1150

print(rotationsPart2(f)) #result test: 6, input: 6738
