# abc130_dの類題
# 区間の和がK以下になる個数を尺取り法で実装する
N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

right = 0
total = 0
cnt = 0
for left in range(N):
    while right < N and total + a[right] <= K:
        total += a[right]
        right += 1

    cnt += right - left

    if left == right:
        right += 1
    else:
        total -= a[left]

print(cnt)