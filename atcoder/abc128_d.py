import sys
readline = sys.stdin.readline
N, K =  list(map(int, readline().split()))
deque = list(map(int, readline().split()))

items = []
ans = 0
for l in range(K+1):
    for m in range(K - l + 1):
        if l + m > N: break
        litems = deque[0:l]
        mitems = deque[N-m:]
        arr = litems + mitems
        arr.sort()
        items.append(arr)

        d = K - l - m
        for n in range(min(len(arr), d+1)):
            ans = max(ans, sum(arr[n:]))

print(ans)