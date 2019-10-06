# 部分和数え上げ
# https://qiita.com/drken/items/a5e6fe22863b7992efdb#問題-4部分和数え上げ問題
N = int(input())
a = list(map(int, input().split()))
A = int(input())
dp = [[False]*(A+1) for _ in range(N+1)]
a = [0] + a 
dp[0][0] = 1

for i in range(N):
    for j in range(A + 1):
        dp[i + 1][j] = dp[i][j]
        if j >= a[i + 1]:
            dp[i + 1][j] = dp[i + 1][j] + dp[i][j - a[i + 1]]

print(dp[-1][A] % 1000000009)