N, T = list(map(int, input().split()))
ct = []
for i in range(N):
    c, t = list(map(int, input().split()))
    ct.append([c, t])

ans = 1000000007
for i in range(N):
    if ct[i][1] <= T:
        ans = min(ans, ct[i][0])

print(ans) if ans != 1000000007 else print('TLE')