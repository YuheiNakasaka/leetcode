# O(N * log(Xn))
from bisect import bisect_left
import sys
readline = sys.stdin.readline
N = int(readline())
X = [int(x) for x in readline().split()]

# X = [i for i in range(2*10**5)]
# N = len(X)

sX = sorted(X)
m = (N - 1) // 2
for i in range(N):
    p = bisect_left(sX, X[i])
    if p <= m:
        print(sX[m + 1])
    else:
        print(sX[m])
