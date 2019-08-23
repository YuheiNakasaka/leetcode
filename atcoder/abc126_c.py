import sys
import math
readline = sys.stdin.readline
N, K = list(map(int, readline().split()))

ans = 0
for i in range(1, N+1):
        now = i
        tmp = 1/N
        while now < K:
            now = now * 2
            tmp = tmp / 2
        ans += tmp

print(ans)