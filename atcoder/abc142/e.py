# import sys
# readline = sys.stdin.readline
# N,M = list(map(int, readline().split()))

# aa = []
# aaa = [[] for i in range(N)]
# for i in range(M):
#     a, b = list(map(int, readline().split()))
#     c = list(map(int, readline().split()))
#     aa.append(a)
#     for j in range(b):
#         aaa[c[j]-1].append(i)

# # print(aaa)

# pats = []
# def dfs(arr,depth):
#     if depth == N:
#         return pats.append(arr)
#     for i in range(len(aaa[depth])):
#         tmp = aaa[depth][i]
#         dfs(arr + [tmp], depth + 1)

# dfs([], 0)
# # print(pats)
# ans = -1
# for i in range(len(pats)):
#     if len(pats[i]) == N:
#         if ans == -1:
#             ans = (10**5)*12
#         s = 0
#         idx = set(pats[i])
#         for j in idx:
#             s += aa[j]
#         ans = min(s, ans)

# print(ans)

n, m = map(int, input().split())
ac = []
for _ in range(m):
    a, _ = map(int, input().split())
    c = sum([2**(int(i)-1) for i in input().split()])
    ac.append([a, c])
dp = [float('inf')] * 2**n
dp[0] = 0
for s in range(2**n):
    for a, c in ac:
        t = s|c
        if dp[t] > dp[s] + a:
            dp[t] = dp[s] + a
print(ac, dp)
ans = dp[-1]
if ans == float('inf'):
    ans = -1
print(ans)
