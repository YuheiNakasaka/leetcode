import sys
readline = sys.stdin.readline
n,m = list(map(int, readline().split()))
py = []
for _ in range(m):
    py.append(list(map(int, readline().split())))

spy = sorted(py, key=lambda x: x[1])

Y = {}
for i in range(m):
    Y[spy[i][1]] = 0

P = [0 for _ in range(n+1)]

for i in range(m):
    P[spy[i][0]] += 1
    Y[spy[i][1]] = P[spy[i][0]]

for i in range(m):
    print(str(py[i][0]).zfill(6) + str(Y[py[i][1]]).zfill(6))

# 頭良い...
# import sys
 
# stdin = sys.stdin
 
# ni = lambda: int(ns())
# na = lambda: list(map(int, stdin.readline().split()))
# ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces
 
# n, m = na()
# pys = []
# for i in range(m):
#     x = na()
#     x = [x[0], x[1], i]
#     pys.append(x)
 
# pys.sort()
# pp = -1
# lid = 0
# ans = [0] * m
# for i in range(m):
#     if pys[i][0] == pp:
#         lid += 1
#     else:
#         lid = 1
#     ans[pys[i][2]] = pys[i][0] * 1000000 + lid
#     pp = pys[i][0]
# for v in ans:
#     print("{:012d}".format(v))