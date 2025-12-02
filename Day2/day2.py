# Source - https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-equal
# Posted by kennytm, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-02, License - CC BY-SA 4.0
from itertools import groupby
def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)
#

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

def invalidIdPart2(line: str) -> int:
    sum = 0
    line = line.split(',')

    for ran in line:
        ranges = ran.split('-')
        inital = int(ranges[0])
        end = int(ranges[1])
        i = inital
        while (i <= end):
            for mult in range(2, len(str(i)) + 1):
                if (len(str(i)) % mult == 0):
                    listy = []
                    for m in range(mult):
                        listy.append(str(i)[int(m*int(len(str(i))/mult)) : int((m+1)*int(len(str(i))/mult))])
                    #print(str(mult) + " " + str(m))
                    #print(listy)

                    if all_equal(listy.__iter__()):
                        sum += i
                        break
                    
            i += 1

    return sum


f = open("input.txt")
#f = open("test.txt")

#print(invalidIdPart1(f.read())) #result test: 1227775554, input: 9188031749

print(invalidIdPart2(f.read())) #result test: 4174379265, input: 11323661261
