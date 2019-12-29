import sys
readline = sys.stdin.readline
N = int(readline())
t = []
x = []
y = []
for i in range(N):
    _t, _x, _y = list(map(int, readline().split()))
    t.append(_t)
    x.append(_x)
    y.append(_y)

p = [0, 0]
pt = 0
px = 0
py = 0
f = True
for i in range(N):
    a = t[i] - pt
    b = abs(px - x[i]) + abs(py - y[i])
    # 距離が足りないかt~t+1間の座標の差のと偶奇が一致しない場合はたどり着けない
    if a < b or (a % 2 != b % 2):
        f = False
        break
    px = x[i]
    py = y[i]
    pt = t[i]

if f == True:
    print('Yes')
else:
    print('No')