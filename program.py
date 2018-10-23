def d_wo_diag(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def d_normal(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2) ** 2) ** 0.5

# reading data
inp = open("input.txt")
pointsCount = int(inp.readline())
array = [[]]  # [] so 0th element present
for line in inp:
    array.append(line.replace('\n', '').split(' '))
inp.close()

# initialization
dist = [0] + [float('inf')] * (pointsCount - 1)  # [0, inf, inf, ...]
parent = [float('NaN')] * pointsCount  # [nan, nan, ...]
queue = list(range(1, pointsCount + 1))
print(array)
print(dist)
print(parent)
print(queue)
# main loop
while queue:
    curP = queue.pop()
    for i in range(1, pointsCount + 1):
        p = array[i]
        if p != curP and p in queue:
            distance = d_wo_diag(p[0], p[1], curP[0], curP[1])
            if distance < dist[p]:
                dist[i] = distance
                parent[i] = p
# outputting data
out = open('output.txt', 'w')
out.close()
