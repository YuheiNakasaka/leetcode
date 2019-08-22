N, M = list(map(int, input().split()))
lr = []
for i in range(M):
    l, r = list(map(int, input().split()))
    lr.append([l, r])

mi = -1
ma = 10**5 + 1
for i in range(M):
    l = lr[i][0]
    r = lr[i][1]
    if mi <= l:
        mi = l
    if r <= ma:
        ma = r

ans = ma - mi + 1
print(ans)if ans >= 0 else print(0)