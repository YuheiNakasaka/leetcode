# https://qiita.com/drken/items/a5e6fe22863b7992efdb
# 問題 1
n = int(input())
a = list(map(int, input().split()))

dp = [0 for i in range(n+1)]

dp[0] = 0

for i in range(n):
    dp[i + 1] = max(dp[i], dp[i] + a[i])

print(max(dp))