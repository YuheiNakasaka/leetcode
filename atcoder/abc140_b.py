N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split())) + [0]

ans = 0

for i in range(N):
    k = A[i] - 1
    ans += B[k]

for i in range(N - 1):
    k = A[i] - 1
    if A[i] + 1 == A[i + 1]:
        ans += C[k]

print(ans)