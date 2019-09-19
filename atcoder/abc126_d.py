# ダメな例
# import sys
# readline = sys.stdin.readline

# n = int(input())
# tree = [[] for _ in range(n+1)]
# for i in range(n-1):
#     u1, u2, l = list(map(int, readline().split()))
#     tree[u1].append([u2, l])

# ans = [0 for _ in range(n+1)]
# for i in range(n+1):
#     if len(tree[i]) == 0: continue
#     for j in range(len(tree[i])):
#         if tree[i][j][1] % 2 == 0:
#             ans[i] = 1
#             ans[tree[i][j][0]] = 1
#         else:
#             if ans[i] == 1:
#               ans[tree[i][j][0]] = 0
#             else:
#               ans[tree[i][j][0]] = 1
# # print(tree)
# # print(ans)

# for i in ans[1:]:
#     print(i)

# 提出7356090のコード
from collections import deque
 
 
def main():
    # 幅優先探索
    def bfs():
        q = deque([0])
        while q:
            u = q.popleft()
            # 接続頂点を精査
            for v, w in g[u]:
                # まだチェックしていない頂点をチェック
                if color[v] == -1:
                    q.append(v)
                    # 偶数なら同じ色で塗る
                    if w == 0:
                        color[v] = color[u]
                    else:
                        color[v] = color[u] ^ 1
 
    n = int(input())
    g = [[] for _ in range(n)]
    # 塗りつぶし結果
    color = [-1] * n
    # スタートは黒で塗っておく
    color[0] = 1
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        w %= 2
        g[u].append((v, w))
        g[v].append((u, w))
    # gは[(根の番号,距離の偶奇)]のデータ構造

    bfs()
    print(*color)
 
 
if __name__ == "__main__":
    main()