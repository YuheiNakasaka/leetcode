import sys
sys.setrecursionlimit(10**6)

N, Q = list(map(int, input().split()))
# 双方向に張る
tree = [[] for _ in range(N)]
for i in range(N-1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

# queryのスコア表を作る
total = [0 for _ in range(N)]
for i in range(Q):
    p, x = list(map(int, input().split()))
    total[p - 1] += x

# dfs
ans = [0 for _ in range(N)]
def dfs(v, p, value):
    value += total[v]
    ans[v] = value
    for c in tree[v]:
        if c == p: continue
        dfs(c, v, value)

dfs(0, -1, 0)
print(" ".join(list(map(str, ans))))