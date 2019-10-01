import sys
readline = sys.stdin.readline

N,K = list(map(int, input().split()))
h = list(map(int, input().split()))
h.sort(key=lambda x: -x)

ans = 0

for i in range(N):
    if h[i] >= K:
        ans += 1

print(ans)
