# 3
# 1 0 0
N = int(input())
a = list(map(int, input().split()))

a = [0] + a
b = [0 for i in range(N+1)]
i = N
while i > 0:
    s = sum(b[i::i])
    if a[i] != s % 2:
        b[i] = 1
    i -= 1

print(sum(b))
for i, j in enumerate(b):
    if j == 1:
        print(i, end=' ')