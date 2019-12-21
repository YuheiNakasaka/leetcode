N = int(input())
A = list(map(int, input().split()))

A = [0] + A + [0]
total = 0
for i in range(N + 2 -1):
    total += abs(A[i] - A[i+1])

for i in range(1, N + 2 - 1):
    t1 = abs(A[i-1] - A[i]) + abs(A[i] - A[i+1])
    t2 = abs(A[i-1] - A[i+1])
    print(total - t1 + t2)