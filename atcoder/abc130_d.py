N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

right = 0
total = 0
cnt = 0
for left in range(N):
    while total < K:
        if right == N: break
        total += a[right]
        right += 1
    if total >= K:
        cnt += N - right + 1
    total -= a[left]
print(cnt)