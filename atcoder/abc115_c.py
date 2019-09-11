import sys
readline = sys.stdin.readline
N, K = list(map(int, readline().split()))
h = []
for _ in range(N):
    h.append(int(readline()))

h.sort()

L = 0
resp = 10**9 + 1
while L + K <= N:
    b = h[L + K - 1] - h[L]
    if resp > b:
        resp = b
    # print(h[L + K - 1],h[L],resp)
    L += 1

print(resp)