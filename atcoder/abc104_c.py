# 全探索じゃダメ
# D, G = list(map(int, input().split()))
# pa = []
# for i in range(D):
#     p, c = list(map(int, input().split()))
#     tmp = [[0, 0]]
#     for j in range(p):
#         score = (i + 1) * 100 * (j + 1)
#         if j + 1 == p:
#           tmp.append([score + c, j + 1])
#         else:
#           tmp.append([score, j + 1])
#     pa.append(tmp)

# allPat = []
# def dfs(arr, picks, depth):
#     if depth == D:
#         total = 0
#         cnt = 0
#         for i in range(len(picks)):
#             total += picks[i][0]
#             cnt += picks[i][1]
#         allPat.append([total, cnt])
#         return picks
#     for a in arr[depth]:
#         tmp = picks + [a]
#         dfs(arr, tmp, depth + 1)

# dfs(pa, [], 0)
# print(1)
# ans = 10**9
# for item in allPat:
#     if item[0] >= G:
#         ans = min(ans, item[1])

# print(ans)

# ボーナスの組み合わせを2^Dだけ全部調べていく
from itertools import product

D, G = map(int, input().split())
score = []
for i in range(D):
    p, c = map(int, input().split())
    s = (i + 1) * 100
    score.append([s, p, c, s * p + c])

ans = float('inf')
for ptn in product([0, 1], repeat=D):
    total = 0
    cnt = 0
    for i in range(D):
        total += score[i][3] * ptn[i]
        cnt += score[i][1] * ptn[i]

    if 0 in ptn[::-1]:
        i = D - 1 - ptn[::-1].index(0)
        x = score[i]
    else:
        x = score[-1]

    for i in range(x[1]):
        if total >= G:
            break
        total += x[0]
        cnt += 1

    if total < G:
        cnt = float('inf')
    ans = min(ans, cnt)
print(ans)
