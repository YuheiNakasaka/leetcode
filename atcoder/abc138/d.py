import sys
sys.setrecursionlimit(10**6)

readline = sys.stdin.readline
n, q = list(map(int, readline().split()))
# 双方向に張る
tree = [[] for _ in range(n)]
for i in range(n-1):
    a, b = list(map(int, readline().split()))
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

# queryのスコア表を作る
total = [0 for _ in range(n)]
for i in range(q):
    p, x = list(map(int, readline().split()))
    total[p - 1] += x

# dfs
ans = [0 for _ in range(n)]
def dfs(v, p, value):
    value += total[v]
    ans[v] = value
    for c in tree[v]:
        if c == p: continue
        dfs(c, v, value)

dfs(0, -1, 0)
print(*ans)