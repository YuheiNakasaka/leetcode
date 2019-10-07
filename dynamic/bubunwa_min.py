N = int(input())
a = list(map(int, input().split()))
A = int(input())

INF = 10**9
dp = [[INF] * (A+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(A + 1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j - a[i] >= 0:
            dp[i+1][j] = min(dp[i][j - a[i]] + 1, dp[i+1][j])

print(dp[-1][-1])
