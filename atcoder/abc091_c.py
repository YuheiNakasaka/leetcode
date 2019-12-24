import sys
import bisect
r = sys.stdin.readline
N = int(r())
red = []
blue = []
for i in range(N):
    a, b = list(map(int, r().split()))
    red.append([a, b])
for i in range(N):
    c, d = list(map(int, r().split()))
    blue.append([c, d])

xblue = sorted(blue, key=lambda x: x[0])

i = 0
j = 0
ii = [True for i in range(2*N+1)]
jj = [True for i in range(2*N+1)]
ans = 0
for i in range(N):
    m = [-100000, -100000]
    for j in range(N):
        if ii[i] and jj[j] and red[j][0] < xblue[i][0] and red[j][1] < xblue[i][1]:
            if m[0] < red[j][1]:
                m[0] = red[j][1]
                m[1] = j
    if m[0] != -100000 and m[1] != -100000:
        ii[i] = False
        jj[m[1]] = False
        ans += 1

print(ans)