
def joltage(length:int, f):
    sum = 0
    for line in f:
        line = line.strip('\n')
        digitsArray = []
        index = 0
        for i in range(length):
            rangeLeft = len(line) - (length-1-i) - index
            digitsArray.append(line[index])
            for j in range(index, index + rangeLeft):
                if digitsArray[i] < line[j]:
                    index = j
                    digitsArray[i] = line[j]
            index += 1
        num = 0
        for i in range(length):
            num *= 10
            num += int(digitsArray[i])
        sum += num
    return sum


#f = open("input.txt")
f = open("test.txt")

#print(joltage(2, f)) #result test: 357, input: 16993
print(joltage(12, f)) #result test: 3121910778619, input: 168617068915447
