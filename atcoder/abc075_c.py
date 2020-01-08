# 発想はわかったが実装まで出来なかった
N, M = list(map(int, input().split()))
ab = []
for i in range(M):
    ab.append(list(map(int, input().split())))

ans = 0

def dfs(x):
    visited[x] = True
    for i in range(len(graph[x])):
        if visited[graph[x][i]]:
            continue
        else:
            dfs(graph[x][i])

for i in range(M):
    visited = [False for k in range(N + 1)]
    visited[0] = True
    graph = [[] for k in range(N + 1)]
    for j in range(M):
        if j != i:
            graph[ab[j][0]].append(ab[j][1])
            graph[ab[j][1]].append(ab[j][0])
    dfs(1)

    for j in range(N + 1):
        if visited[j]:
            continue
        else:
            ans += 1
            break

print(ans)