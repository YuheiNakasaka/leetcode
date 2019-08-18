# 6 2
# 1 2
# 1 3
# 2 4
# 3 6
# 2 5
# 1 10
# 1 10
# 6 2 {1: [2, 3], 2: [4, 5], 3: [6]} [[1, 10], [1, 10]]
N, Q = list(map(int, input().split()))
tree = {}
for i in range(N-1):
    a, b = list(map(int, input().split()))
    items = tree.get(a, [])
    items.append(b)
    tree[a] = items

q = []
for i in range(Q):
    q.append(list(map(int, input().split())))

ans = [0] * (N + 1)

def recc_sum(p, x, tree_p):
    for i in range(len(tree_p)):
        index = tree_p[i]
        ans[index] += x
        if tree.get(index, None) != None:
            recc_sum(index, x, tree[index])

for i in range(Q):
    p = q[i][0]
    x = q[i][1]
    ans[p] += x
    if tree.get(p, None) != None:
        recc_sum(p, x, tree[p])

print(" ".join(list(map(str, ans[1:]))))