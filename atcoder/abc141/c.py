import sys
readline = sys.stdin.readline

n, k, q = list(map(int, readline().split()))
a = [(k - q) for i in range(n)]
for i in range(q):
    a[int(readline())-1] += 1

for i in range(n):
    if a[i] > 0:
        print('Yes')
    else:
        print('No')
