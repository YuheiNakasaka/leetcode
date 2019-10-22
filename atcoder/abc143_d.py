import sys
import bisect
readline = sys.stdin.readline
N = int(readline())
L = list(map(int, readline().split()))
L.sort()

ans = 0
for i in range(N):
    for j in range(i, N):
        if i == j: continue
        ab = L[i] + L[j]
        to = bisect.bisect_left(L, ab, j, N)
        ans += to - 1 - j
print(ans)