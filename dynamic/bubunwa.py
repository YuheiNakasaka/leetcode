# 部分和
# https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E5%95%8F%E9%A1%8C-3%E9%83%A8%E5%88%86%E5%92%8C%E5%95%8F%E9%A1%8C
N = int(input())
a = list(map(int, input().split()))
A = int(input())
dp = [[False]*(A+1) for _ in range(N+1)]
a = [0] + a 
dp[0][0] = True

for i in range(N):
    for j in range(A + 1):
        dp[i + 1][j] |= dp[i][j]
        if j >= a[i + 1]:
            dp[i + 1][j] = dp[i + 1][j] | dp[i][j - a[i + 1]]

print("YES") if True in [dp[i][10] for i in range(N+1)] else print("No")