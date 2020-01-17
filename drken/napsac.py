n, W = list(map(int, input().split()))
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

dp = [[0]*10010 for i in range(n+1)]

for i in range(n):
    for w in range(W):
        weight = p[i][0]
        value = p[i][1]
        if w >= weight:
            dp[i + 1][w] = max(dp[i][w - weight] + value, dp[i][w])
        else:
            dp[i + 1][w] = dp[i][w]

print(dp[n][W-1])
