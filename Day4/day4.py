def matrixFromFile(f):
    matrix = []
    for line in f:
        line = line.strip('\n')
        m = []
        for p in line:
            m.append(p)
        matrix.append(m)
    return matrix

def validMatrixCoords(x:int, y:int, w:int, h:int) -> bool:
    if (x < 0 or y < 0):
        return False
    if (x >= w or y >= h):
        return False
    return True

def PaperCountPart1(matrix):
    sum = 0
    height = len(matrix)
    width = len(matrix[0])
    for j in range(height):
        for i in range(width):
            if (matrix[j][i] == '@'):
                count = 0
                if (validMatrixCoords(i-1,j-1,width,height) and matrix[j-1][i-1] == '@'):
                    count += 1
                if (validMatrixCoords(i,j-1,width,height) and matrix[j-1][i] == '@'):
                    count += 1
                if (validMatrixCoords(i+1,j-1,width,height) and matrix[j-1][i+1] == '@'):
                    count += 1
                if (validMatrixCoords(i-1,j,width,height) and matrix[j][i-1] == '@'):
                    count += 1
                if (validMatrixCoords(i+1,j,width,height) and matrix[j][i+1] == '@'):
                    count += 1
                if (validMatrixCoords(i-1,j+1,width,height) and matrix[j+1][i-1] == '@'):
                    count += 1
                if (validMatrixCoords(i,j+1,width,height) and matrix[j+1][i] == '@'):
                    count += 1
                if (validMatrixCoords(i+1,j+1,width,height) and matrix[j+1][i+1] == '@'):
                    count += 1
                if (count < 4):
                    sum += 1
    return sum

def PaperCountPart2(matrix):
    sum = 0
    height = len(matrix)
    width = len(matrix[0])

    removedSomePaper = True

    while removedSomePaper:
        minisum = 0
        for j in range(height):
            for i in range(width):
                if (matrix[j][i] == '@'):
                    count = 0
                    if (validMatrixCoords(i-1,j-1,width,height) and matrix[j-1][i-1] == '@'):
                        count += 1
                    if (validMatrixCoords(i,j-1,width,height) and matrix[j-1][i] == '@'):
                        count += 1
                    if (validMatrixCoords(i+1,j-1,width,height) and matrix[j-1][i+1] == '@'):
                        count += 1
                    if (validMatrixCoords(i-1,j,width,height) and matrix[j][i-1] == '@'):
                        count += 1
                    if (validMatrixCoords(i+1,j,width,height) and matrix[j][i+1] == '@'):
                        count += 1
                    if (validMatrixCoords(i-1,j+1,width,height) and matrix[j+1][i-1] == '@'):
                        count += 1
                    if (validMatrixCoords(i,j+1,width,height) and matrix[j+1][i] == '@'):
                        count += 1
                    if (validMatrixCoords(i+1,j+1,width,height) and matrix[j+1][i+1] == '@'):
                        count += 1
                    if (count < 4):
                        minisum += 1
                        matrix[j][i] = '.'
        sum += minisum
        if minisum == 0:
            removedSomePaper = False
    return sum

f = open("input.txt")
#f = open("test.txt")

#print(PaperCountPart1(matrixFromFile(f))) #result test: 13, input: 1428
print(PaperCountPart2(matrixFromFile(f))) #result test: 43, input: 8936
