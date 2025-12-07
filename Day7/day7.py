
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



f = open("input.txt")
#f = open("test.txt")

print(TachyonBeamsPart1(f)) #result test: 21, input: 1600
#print(TachyonBeamsPart2(f)) #result test: , input: 
