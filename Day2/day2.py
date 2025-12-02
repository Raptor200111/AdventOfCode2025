def invalidIdPart1(line: str) -> int:

    sum = 0
    line = line.split(',')

    for range in line:
        ranges = range.split('-')
        inital = int(ranges[0])
        end = int(ranges[1])
        i = inital
        while (i <= end):
            if len(str(i))%2 == 0:
                length = len(str(i)) / 2
                firstDigit = int(i / pow(10, length))
                secondDigit = int(i % pow(10, length))
                if firstDigit == secondDigit:
                    sum += i
            i += 1

    return sum

def invalidIdPart2(f):
    nz = 0
    

    return nz


f = open("input.txt")
#f = open("test.txt")

print(invalidIdPart1(f.read())) #result test: 1227775554, input: 

#print(invalidIdPart2(f)) #result test: 6, input: 6738
