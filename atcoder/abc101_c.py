N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

m = 10**8
idx = 0
for i in range(N):
    if A[i] < m:
        m = A[i]
        idx = i

cnt = 0
i = 0
while i < N - 1:
    i += K - 1
    cnt += 1

print(cnt)