# だめ
N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i, N):
        if sum(a[i:j+1]) >= K:
            cnt += 1
print(cnt)