N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for i in range(N):
    y = ans + (V[i] - C[i])
    if ans < y:
        ans = y

print(ans)
