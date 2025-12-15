def dist2(j1, j2):
    return sum((j1[k] - j2[k])**2 for k in range(3))

def LargestCircuitsPart1(f, quant):
    points = []
    for line in f:
        points.append( tuple(map(int, line.strip().split(','))) )

    union_map = {}
    class Union:
        def __init__(self, members):
            self.members = members
            for m in members:
                union_map[m] = self
        def union(self, other):
            new_members = self.members | other.members
            return Union(new_members)

    for i in range(len(points)):
        Union({i})
    #for p in points:
    #    Union({p})

    allConnections = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
                allConnections.append((i, j))
    allConnections.sort(key=lambda pair: dist2(points[pair[0]], points[pair[1]]))

    #for pair in allConnections[:quant]:
    #    print(pair)

    for i, (p, q) in enumerate(allConnections):
        # part 1
        if i == (quant):
            unions = set()
            for i in range(len(points)):
                unions.add(union_map[i])
            unions = list(sorted(unions, key=lambda u: len(u.members), reverse=True))
            return len(unions[0].members) * len(unions[1].members) * len(unions[2].members)
        if union_map[p] == union_map[q]:
            continue
        u = union_map[p].union(union_map[q])

    return 0


def LargestCircuitsPart2(f):
    points = []
    for line in f:
        points.append( tuple(map(int, line.strip().split(','))) )

    union_map = {}
    class Union:
        def __init__(self, members):
            self.members = members
            for m in members:
                union_map[m] = self
        def union(self, other):
            new_members = self.members | other.members
            return Union(new_members)

    for i in range(len(points)):
        Union({i})
    #for p in points:
    #    Union({p})

    allConnections = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
                allConnections.append((i, j))
    allConnections.sort(key=lambda pair: dist2(points[pair[0]], points[pair[1]]))

    #for pair in allConnections[:quant]:
    #    print(pair)

    for i, (p, q) in enumerate(allConnections):
        if union_map[p] == union_map[q]:
            continue
        u = union_map[p].union(union_map[q])
        if len(u.members) == len(points):
            return points[p][0]*points[q][0]

    return 0

#f = open("test.txt")
#print(LargestCircuitsPart1(f, 10)) #result test: 40
#print(LargestCircuitsPart2(f)) #result test: 25272

f = open("input.txt")
#print(LargestCircuitsPart1(f, 1000)) #result input: 163548
print(LargestCircuitsPart2(f)) #result input: 772452514