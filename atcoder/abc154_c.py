N = int(input())
A = list(map(int, input().split()))

h = {}
ans = 'YES'
for i in range(N):
    a = h.get(A[i], 0)
    if a != 0:
        ans = 'NO'
        break
    h[A[i]] = A[i]

print(ans)