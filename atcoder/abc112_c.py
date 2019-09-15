n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

# h=0の点を選んではいけない。なぜならh=0で計算するとピラミッドの頂点が1以上の点が複数存在できてしまうので。
a = sorted(a, key=lambda x: -x[2])

m = 0
mx = 0
my = 0

for cx in range(101):
    for cy in range(101):
        flag = True
        x, y, h = a[0]
        H = max(abs(x-cx) + abs(y-cy) + h, 0)
        for i in range(n):
            xx, yy, hh = a[i]
            if hh != max(H - abs(xx - cx) - abs(yy - cy), 0):
                flag = False

        if flag == True:
            mx = cx
            my = cy
            m = H

print(str(mx) + ' ' + str(my) + ' ' + str(m))
