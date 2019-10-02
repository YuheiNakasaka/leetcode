# N W
# value weight
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp

N, W = list(map(int, input().split()))
products = []
mw = 1
for i in range(N):
    v, w = list(map(int, input().split()))
    mw += w
    products.append([w, v])

# print(products)

dp = [[0] * mw for i in range(N+1)]

# print(dp)

for i in range(N):
    for w in range(W + 1):
        if w >= products[i][0]:
            dp[i+1][w] = max(dp[i][w - products[i][0]] + products[i][1], dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]

# print(dp)

print(max(dp[N]))