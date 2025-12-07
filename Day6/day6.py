
def CephalopodMathPart1(f):
    matrix = []
    for line in f:
        line = line.strip()
        numbers = line.split()
        if matrix == []:
            for n in numbers:
                matrix.append([n])
        else:
            i = 0
            for n in numbers:
                matrix[i].append(n)
                i+=1
    sum = 0
    for m in matrix:
        last = len(m) - 1
        sign = m[last]
        m.pop(last)
        summ = 0
        if sign == '*':
            for num in m:
                if summ == 0:
                    summ = int(num)
                else:
                    summ *= int(num)
        elif sign == '+':
            for num in m:
                summ += int(num)
        sum += summ
    return sum

def CephalopodMathPart2(f):
    sum = 0
    matrix = []

    line = f.readline().strip('\n')

    while line != "":
        if line[0] == '*' or line[0] == '+':
            break
        matrix.append(line)
        line = f.readline().strip('\n')

    signs = line
    lastSign = ' '
    numbers = []
    for i in range(len(matrix[0])):
        if signs[i] == '*' or signs[i] == '+':
            lastSign = signs[i]
        
        allSpaces = True

        for j in range(len(matrix)):
            if matrix[j][i] != ' ':
                allSpaces = False
                break

        if allSpaces:
            summ = 0
            if lastSign == '*':
                for n in numbers:
                    if summ == 0:
                        summ = n
                    else:
                        summ *= n
            elif lastSign == '+':
                for n in numbers:
                    summ += n
            sum += summ
            numbers = []
        else:
            num = 0
            for j in range(len(matrix)):
                if matrix[j][i] != ' ':
                    num *= 10
                    num += int(matrix[j][i])
            numbers.append(num)

        if i == len(matrix[0])-1:
            summ = 0
            if lastSign == '*':
                for n in numbers:
                    if summ == 0:
                        summ = n
                    else:
                        summ *= n
            elif lastSign == '+':
                for n in numbers:
                    summ += n
            sum += summ
            numbers = []


    #print(matrix)
    return sum

f = open("input.txt")
#f = open("test.txt")

#print(CephalopodMathPart1(f)) #result test: 4277556, input: 5322004718681
print(CephalopodMathPart2(f)) #result test: 3263827, input: 9876636978528
