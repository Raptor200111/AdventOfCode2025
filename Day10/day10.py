import ast
from io import TextIOWrapper
from itertools import product

def Combinations(buttonList, length):
    return list(product(buttonList, repeat=length))

def PosibleCombination(solution, combination):
    lights = [False] * len(solution)
    for c in combination:
        if isinstance(c, tuple):
            for n in c:
                lights[n] = not lights[n]
        else:
            lights[c] = not lights[c]
    #i = 0
    return solution == lights

def FactoryMachinesPart1(f: TextIOWrapper):
    sum = 0
    for line in f:
        line = line.strip().split(' ')
        lightSolution = [False] * (len(line[0]) - 2)
        for i in range(len(line[0]) - 2):
            if line[0][i+1] == '#':
                lightSolution[i] = True
        
        #joltageReqs = line[len(line)-1] #useless for now
        line.pop(0)
        #print(lightSolution)

        line.pop(len(line)-1)
        line = list(map(ast.literal_eval, line))
        #print(line)
        solutionFound = False
        lenghtTested = 0
        while not solutionFound:
            lenghtTested += 1
            posibleSolutions = Combinations(line, lenghtTested)
            for ps in posibleSolutions:
                if PosibleCombination(lightSolution, ps):
                    solutionFound = True
                    break
        sum += lenghtTested
        
        #print(joltageReqs)
    return sum

def FactoryMachinesPart2(f):
    return 0

f = open("input.txt")
#f = open("test.txt")

print(FactoryMachinesPart1(f)) #result test: 7, input: 469
#print(FactoryMachinesPart2(f)) #result test: , input: 