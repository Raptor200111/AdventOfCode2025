from io import TextIOWrapper

def RecursiveSearchWithMemo(idx, connections, memo):
    if idx == "out":
        return 1
    
    if idx in memo:
        return memo[idx]

    sum = 0
    for way in connections[idx]:
        sum += RecursiveSearchWithMemo(way, connections, memo)

    memo.update({idx: sum})
    return sum

def ReactorPart1(f: TextIOWrapper):
    
    connections = {}
    for line in f:
        
        line = line.strip().split(':')
        connections.update({line[0]: line[1].strip().split(' ')})

    memo = {}
    return RecursiveSearchWithMemo("you", connections, memo)

def ReactorPart2(f):
    return 0


f = open("input.txt")
#f = open("test.txt")

print(ReactorPart1(f)) #result test: 5, input: 
#print(ReactorPart2(f)) #result test: , input: 
