def dist_manhattan(x1, y1, x2, y2):
    return abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))


# reading data
inp = open("input.txt")
pointsCount = int(inp.readline())
array = []
for line in inp:
    array.append(line.replace('\n', '').split(' '))
inp.close()

# initialization
dist = [0] + [float('inf')] * (pointsCount - 1)  # [0, inf, inf, ...]
parent = [float('NaN')] * pointsCount  # [nan, nan, ...]
queue = list(range(1, pointsCount))
added = [0]

# main loop
for curPointIndex in queue:
    for treePointIndex in range(0, pointsCount):
        if treePointIndex != curPointIndex and parent[treePointIndex] != curPointIndex and treePointIndex in added:
            distance = dist_manhattan(array[treePointIndex][0], array[treePointIndex][1],
                                      array[curPointIndex][0], array[curPointIndex][1])
            if distance < dist[curPointIndex]:
                dist[curPointIndex] = distance
                parent[curPointIndex] = treePointIndex
                added.append(curPointIndex)

# outputting data
print(array)
print(parent)
print(dist)
out = open('output.txt', 'w')
for i in range(0, pointsCount):
    out.write(str(i + 1)+' ')
    for j in range(0, pointsCount):
        if parent[j] == i or parent[i] == j:
            out.write(str(j + 1)+' ')
    out.write('\n')
out.write(str(sum(dist)))
out.close()
