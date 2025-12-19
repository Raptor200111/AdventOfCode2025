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

def RecursiveSearchWithMemo2(idx: str, connections: dict, memo: dict, dacFound: bool, fftFound: bool):
    if idx == "dac":
        dacFound = True
    if idx == "fft":
        fftFound = True

    if idx == "out":
        return 1 if dacFound and fftFound else 0
    
    key = (idx, dacFound, fftFound)
    if key in memo:
        return memo[key]

    sum = 0
    for way in connections[idx]:
        sum += RecursiveSearchWithMemo2(way, connections, memo, dacFound, fftFound)

    memo[key] = sum
    return sum

def ReactorPart2(f: TextIOWrapper):
    connections = {}
    for line in f:
        line = line.strip().split(':')
        connections.update({line[0]: line[1].strip().split(' ')})

    memo = {}
    return RecursiveSearchWithMemo2("svr", connections, memo, False, False)
    


f = open("input.txt")
#f = open("test.txt")
#f = open("test2.txt")


#print(ReactorPart1(f)) #result test: 5, input: 494
print(ReactorPart2(f)) #result test: 2, input: 296006754704850
