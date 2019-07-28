N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total = 0
for i in range(N):
    if A[i] < B[i]:
        total += A[i]
        B[i] = B[i] - A[i]
    elif A[i] >= B[i]:
        total += B[i]
        A[i] = A[i] - B[i]
        B[i] = 0
        continue

    if A[i+1] >= B[i]:
        total += B[i]
        A[i+1] = A[i+1] - B[i]
    elif A[i+1] < B[i]:
        total += A[i+1]
        A[i+1] = 0

print(total)