import math

N = int(input())
p = []
fac = math.factorial(N)
for _ in range(N):
    x, y = list(map(int, input().split()))
    p.append([x, y])

t = []
def dfs(a, b):
    if len(b) == N:
        return t.append(b)
    for i in range(len(a)):
        dfs(a[:i] + a[i+1:], b + [a[i]])
dfs(p, [])
total = 0
for i in range(len(t)):
    for j in range(len(t[i]) - 1):
        total += math.sqrt((t[i][j][0] - t[i][j+1][0]) ** 2 + (t[i][j][1] - t[i][j+1][1]) ** 2)
print(total / fac)