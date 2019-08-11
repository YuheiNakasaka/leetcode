import heapq
N, M = list(map(int, input().split()))
# 報酬を得られるまでの日にち毎に報酬をまとめる
days = [[] for _ in range(M + 1)]
for i in range(N):
    a, b = list(map(int, input().split()))
    if a > M: continue
    days[a].append(b)

reward = []
heapq.heapify(reward)
total = 0
# Mの後ろから報酬を得られるまでの日にちが少ない順に優先度付きキューに入れていく
# O(M * NlogN)で解ける
for i in range(M)[::-1]:
    tasks = days[M - i]
    for task in tasks:
        heapq.heappush(reward, -1 * task)

    if len(reward) > 0:
        total += heapq.heappop(reward) * (-1)

print(total)

# 5 3
# 1 2
# 1 3
# 1 4
# 2 1
# 4 3

# 5 3
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3