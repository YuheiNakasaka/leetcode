# 一番高い花の両隣に同じ高さの花があれば1減らす
# 自分も1減らす
# これを繰り返す
N = int(input())
h = list(map(int, input().split()))
def bury(x):
    for i in range(1,N):
        if x+i >= N or h[x+i] != h[x]:
            break
        else:
            h[x+i] -= 1
    for i in range(1,N):
        if x-i < 0 or h[x-i] != h[x]:
            break
        else:
            h[x-i] -= 1
    h[x] -= 1
    # print(h)
 
ans = 0
while sum(h) > 0:
    bury(h.index(max(h)))
    ans += 1
    
print(ans)