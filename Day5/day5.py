
from ctypes import Array
from io import TextIOWrapper
from typing import List

def LineToRange(line: str) -> Array:
    line = line.split('-')
    return [int(line[0]), int(line[1])]

def RangeIncludesRange(r1: Array, r2: Array) -> bool:
    return (r1[0] <= r2[0] and r1[1] >= r2[1])

def RangeColludesWith(r1: Array, r2: Array) -> bool:
    return (r1[0] <= r2[0] and r1[1] >= r2[0]) or (r1[0] <= r2[1] and r1[1] >= r2[1])

def UniteCollidedRanges(r1: Array, r2: Array) -> Array:
    return [r1[0] if (r1[0] < r2[0]) else r2[0], r1[1] if (r1[1] > r2[1]) else r2[1]]

def key_sum(r):
    return r[0] + r[1]

def NumberWithinRange(n: int, r:Array) -> True:
    return n >= r[0] and n <= r[1]

def orderRanges(f: TextIOWrapper) -> List:
    ranges = []

    line = f.readline().strip('\n')
    while line != "":
        actualRange = LineToRange(line)
        if len(ranges) == 0:
            ranges.append(actualRange)
        else:
            i = 0
            rangeToInclude = True
            while i in range(len(ranges)):
                if RangeIncludesRange(ranges[i], actualRange):
                    rangeToInclude = False
                    break
                elif RangeIncludesRange(actualRange, ranges[i]):
                    ranges.pop(i)
                    continue
                elif RangeColludesWith(ranges[i], actualRange):
                    actualRange = UniteCollidedRanges(ranges[i], actualRange)
                    ranges.pop(i)
                    continue
                i+=1
            if rangeToInclude: 
                ranges.append(actualRange)
                ranges.sort(key=key_sum)
        
        line = f.readline().strip('\n')
    return ranges

def FreshnessPart1(f: TextIOWrapper):
    sum = 0
    ranges = orderRanges(f)

    #print(ranges)
    line = f.readline().strip('\n')
    while line != "":
        for r in ranges:
            if NumberWithinRange(int(line), r):
                sum += 1
                #print(int(line))
                break
        line = f.readline().strip('\n')
    return sum

def FreshnessPart2(f: TextIOWrapper):
    sum = 0
    ranges = orderRanges(f)

    #print(ranges)
    for r in ranges:
        sum += r[1] - r[0] + 1
    return sum

f = open("input.txt")
#f = open("test.txt")

#print(FreshnessPart1(f)) #result test: 3, input: 720
print(FreshnessPart2(f)) #result test: 14, input: 
