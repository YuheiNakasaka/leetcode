N,M = list(map(int, input().split()))
a = []
for i in range(N):
    b = list(map(int, input().split()))
    a.append(b)

c = [0 for i in range(M + 1)]

for i in range(N):
    for j in range(a[i][0] + 1):
        if j == 0: continue
        c[a[i][j]] += 1

ans = 0
for i in range(len(c)):
    if c[i] == N:
        ans += 1

print(ans)