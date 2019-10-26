# 模範解答通りに実装したらPythonだとTLEになった。10*13*10**5だから10**7くらいの計算量になって終わらないっぽい...
# S = list(input())
# sl = len(S)
# dp = [[0] * 13 for _ in range(sl+1)]
# dp[0][0] = 1

# c = ''
# for i in range(sl):
#     if S[i] == '?':
#         c = -1
#     else:
#         c = int(S[i])
#     for j in range(10):
#         if c != -1 and c != j:
#             continue
#         for ki in range(13):
#             dp[i + 1][(ki * 10 + j) % 13] += dp[i][ki] 

# print(dp[-1][5] % (10**9 + 7))

# 代わりにこれ
# https://atcoder.jp/contests/abc135/submissions/8113114
S = str(input())
ans = [0] * 13
ans[0] = 1
MOD = 10**9 + 7
for i in S:
    dp = [0] * 13
    for j in range(13):
        dp[(j * 10) % 13] = ans[j] % MOD
    dp += dp
    if i == '?':
        for j in range(13):
            ans[j] = sum(dp[j+4:j+14])
    else:
        for j in range(13):
            ans[j] = dp[j + 13 - int(i)]
print(ans[5] % MOD)