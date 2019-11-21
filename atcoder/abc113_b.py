N = int(input())
T, A = list(map(int, input().split()))
H = list(map(int, input().split()))

t = 1000000007
ans = 1000000007
for i in range(N):
    u = abs(A - (T - H[i] * 0.006))
    if t > u:
        t = u
        ans = i + 1
print(ans)