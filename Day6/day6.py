
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
    return sum

f = open("input.txt")
#f = open("test.txt")

print(CephalopodMathPart1(f)) #result test: 4277556, input: 
#print(CephalopodMathPart2(f)) #result test: , input: 
