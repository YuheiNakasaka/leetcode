import sys
readline = sys.stdin.readline

N, Q = map(int, readline().split())
S = readline()
t = [0] * (N + 1)
for i in range(N):
    t[i + 1] = t[i] + (1 if S[i : i + 2] == 'AC' else 0)
for i in range(Q):
    l, r = map(int, readline().split())
    print(t[r-1] - t[l-1])