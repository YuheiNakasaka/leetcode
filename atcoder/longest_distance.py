# 3
# 1 1
# 2 4
# 4 3
import math
points = []
length = int(input())
for i in range(length):
    x, y = map(int, input().split())
    points.append([x, y])

distance = 0
for i in range(length):
    for j in range(length):
        d = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
        if d > distance:
            distance = d


print("{}\n".format(distance))