N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    total = 0
    for j in range(M):
        total += B[j] * A[i][j]
    if total + C > 0:
        ans += 1

print(ans)
