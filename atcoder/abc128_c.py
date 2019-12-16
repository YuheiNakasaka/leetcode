N, M = list(map(int, input().split()))
k = [list(map(int, input().split())) for i in range(M)]
p = list(map(int, input().split()))

a = []
def dfs(b):
    if len(b) == N:
        a.append(b)
        return b
    for i in range(2):
        dfs(b + [i])
dfs([])

ans = 0
for i in range(len(a)):
    ok = 0
    switches = a[i]
    for j in range(M):
        on = 0
        for _j in range(k[j][0]):
            if switches[k[j][_j+1]-1] == 1:
                on += 1
        if on % 2 == p[j]:
            ok += 1
    if ok == M:
        ans += 1

print(ans)