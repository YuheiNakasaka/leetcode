import sys
from collections import deque
readline = sys.stdin.readline

n, m = list(map(int, readline().split()))
a = sorted(list(map(int, readline().split())))
bc = []
for _ in range(m):
    b, c = list(map(int, readline().split()))
    bc.append([b * c, c])
bc.sort(key=lambda x: -x[1])
dbc = deque(bc)
for i in range(n):
    if len(dbc) > 0 and a[i] < dbc[0][1]:
        a[i] = dbc[0][1]
        dbc[0][0] -= dbc[0][1]
        if dbc[0][0] == 0:
            dbc.popleft()

print(sum(a))