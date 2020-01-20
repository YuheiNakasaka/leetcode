# 問題を勘違いしてて３回ミスった
N = int(input())
P = list(map(int, input().split()))

ans = 0
bottom = P[0]
for i in range(N):
    if P[i] <= bottom:
        ans += 1
    bottom = min(P[i], bottom)

print(ans)
