import sys
readline = sys.stdin.readline
N, K =  list(map(int, readline().split()))
deque = list(map(int, readline().split()))

items = []
for l in range(K):
    for m in range(K - l + 1):
        if l + m > N: break
        litems = deque[0:l]
        mitems = deque[N-m:]
        arr = litems + mitems
        arr.sort()
        items.append(arr)

ans = 0
for i in range(len(items)):
    item = items[i]
    if len(item) == 0: continue
    d = K - len(item)
    total = sum(item)
    for j in range(d):
        if len(item) <= j: break
        if item[0] >= 0: break
        if item[j] < 0:
            total -= item[j]
            if total > ans:
                ans = total

print(ans)