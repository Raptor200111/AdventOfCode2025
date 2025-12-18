
def TachyonBeamsPart1(f):
    sum = 0
    matrix = []
    for line in f:
        matrix.append(list(line.strip('\n')))
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '|' or matrix[i][j] == 'S':
                if i+1 < len(matrix):
                    if matrix[i+1][j] == '^':
                        if j-1 >= 0:
                            matrix[i+1][j-1] = '|'
                        if j+1 < len(matrix[i+1]):
                            matrix[i+1][j+1] = '|' 
                        sum += 1
                    else:
                        matrix[i+1][j] = '|'
    
    #for m in matrix:
        #print(m)
    return sum

tachyonDictionary = {}

def QuantumTachyonBeams(matrix, x, y):
    i = x
    j = y
    while matrix[j][i] == '|' or matrix[j][i] == 'S':
        if j+1 >= len(matrix):
            return 1
        j += 1
        if matrix[j][i] == '^':
            if (j,i) in tachyonDictionary.keys():
                return tachyonDictionary[(j,i)]
            times = 0
            if i-1 >= 0:
                matrix[j][i-1] = '|'
                times += QuantumTachyonBeams(matrix, i-1, j)
                
            if i+1 < len(matrix[j]):
                matrix[j][i+1] = '|' 
                times += QuantumTachyonBeams(matrix, i+1, j)
            
            tachyonDictionary.update({(j,i): times})
            return times
        else:
            matrix[j][i] = '|'

    return 0


def TachyonBeamsPart2(f):
    matrix = []
    for line in f:
        matrix.append(list(line.strip('\n')))
    i = 0
    for i in range(len(matrix[0])):
        if matrix[0][i] == 'S':
            break
    return QuantumTachyonBeams(matrix, i, 0)

f = open("input.txt")
#f = open("test.txt")

#print(TachyonBeamsPart1(f)) #result test: 21, input: 1600
print(TachyonBeamsPart2(f)) #result test: 40, input: 8632253783011
