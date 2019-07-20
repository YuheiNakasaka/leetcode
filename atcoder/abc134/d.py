# 3
# 1 0 0
N = int(input())
a = list(map(int, input().split()))

M = 0
res = []
for n in range(1, N+1):
    ball = N // n
    if ball % 2 == a[n - 1]:
        M += 1
        res.append(str(a[n - 1]))

print(M)
print(' '.join(res))