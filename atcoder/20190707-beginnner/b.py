import math
N, D = map(int, input().split())

ans = 0
points = []
for n in range(N):
    points.append(list(map(int, input().split())))

i = 0
j = N - 1
while i < N - 1:
    a = points[i]
    b = points[j]
    total = 0
    for d in range(D):
        total += (a[d] - b[d]) ** 2
    res = math.sqrt(total)
    if res.is_integer(): ans += 1
    j -= 1
    if i == j:
        i += 1
        j = N - 1

print(ans)