# 全探索
# 証言が矛盾していないかどうかをチェックする
# 証言の妥当性のみを見れば良い感じ？
N = int(input())
X = []
Y = []
A = []
for i in range(N):
    a = int(input())
    A.append(a)
    b = []
    X_ = []
    Y_ = []

    for j in range(a):
        x, y = list(map(int, input().split()))
        X_.append(x)
        Y_.append(y)
        
    X.append(X_)
    Y.append(Y_)

# bit探索
ans = []
for i in range(2**N):
    a = [0] * N
    cnt = 0
    for j in range(N):
        if i & (1 << j):
            a[j] = 1

    for j in range(N):
        flag = False
        if a[j] == 1:
            for k in range(A[j]):
                if a[X[j][k]-1] != Y[j][k]:
                    flag = True
                    break
        if flag:
            break
    
    if flag == False:
        ans.append(a.count(1))

print(max(ans))