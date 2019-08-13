N, M = list(map(int, input().split(" ")))
a = {}
for i in range(M):
    j = int(input())
    a[j] = 1

# keys = a.keys()
# for i in range(len(keys)):
#     if keys[i] + 1

left = 1
right = 1
cnt = 0
for i in range(1, N):
    if a.get(i, 0) == 1:
        # cnt = left ~ rightの階乗を計算
        left = i + 1
    right += 1

