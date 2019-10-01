import sys
readline = sys.stdin.readline
N = int(readline())
a = list(map(int, readline().split()))

aa = []
for i in range(N):
    tmp = [a[i], i]
    aa.append(tmp)

aa.sort(key=lambda x: x[0])

aaa = []
for i in range(N):
    aaa.append(str(aa[i][1] + 1))

print(' '.join(aaa))

