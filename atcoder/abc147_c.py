N = int(input())
xy = []
for i in range(N):
    a = len(input())
    for j in range(a):
        xy.append(list(map(int, input().split())))

# 全探索
# 証言が矛盾していないかどうかをチェックする
# 証言の妥当性のみを見れば良い感じ？