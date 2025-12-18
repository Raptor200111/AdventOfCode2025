
def LargestRectanglePart1(f):
    points = []
    for line in f:
        points.append( tuple(map(int, line.strip().split(','))) )
    
    widestPoints = [
        [points[0]], #lowest X
        [points[0]], #highest X
        [points[0]], #lowest Y
        [points[0]]  #highest Y
    ]

    maxArea = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            xDif = points[i][0] - points[j][0]
            if xDif < 0: xDif *= -1
            xDif += 1

            yDif = points[i][1] - points[j][1]
            if yDif < 0: yDif *= -1
            yDif += 1

            area = xDif * yDif
            if area > maxArea:
                maxArea = area

    return maxArea

def getVerticalWalls(points):
    verticals = []
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if points[i][0] == points[j][0]:
                y_start = min(points[i][1], points[j][1])
                y_end = max(points[i][1], points[j][1])
                verticals.append((points[i][0], y_start, y_end))
    return verticals

def build_intervals(points, verticals):
    ys = sorted(set(y for _, y in points))
    intervals = []

    for i in range(len(ys) - 1):
        y0 = ys[i]
        y1 = ys[i + 1]
        y_mid = (y0 + y1) / 2

        xs = []
        for x, vy0, vy1 in verticals:
            if vy0 < y_mid < vy1:
                xs.append(x)

        if len(xs) >= 2:
            intervals.append((y0, y1, min(xs), max(xs)))

    return intervals

def LargestRectanglePart2(f):
    points = []
    for line in f:
        points.append(tuple(map(int, line.strip().split(','))))
    
    #verticalsWalls = getVerticalWalls(points)

    intervals = build_intervals(points, getVerticalWalls(points))
    #for it in intervals:
    #   print(it)

    maxArea = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):

            x1, y1 = points[i]
            x2, y2 = points[j]

            x_min = min(x1, x2)
            x_max = max(x1, x2)
            y_min = min(y1, y2)
            y_max = max(y1, y2)

            area = (x_max - x_min + 1) * (y_max - y_min + 1)
            if area <= maxArea:
                continue

            valid = True
            for y0, y1i, xl, xr in intervals:
                # ¿este intervalo vertical intersecta nuestro rectángulo?
                if y1i <= y_min or y0 >= y_max:
                    continue

                if x_min < xl or x_max > xr:
                    valid = False
                    break

            if valid:
                maxArea = area

    return maxArea

#f = open("input.txt")
f = open("test.txt")

#print(LargestRectanglePart1(f)) #result test: 50, input: 4733727792
print(LargestRectanglePart2(f)) #result test: 24, input: 1566346198