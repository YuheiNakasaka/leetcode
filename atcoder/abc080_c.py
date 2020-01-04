N = int(input())
F = []
for i in range(N):
    F.append(list(map(int, input().split())))
P = []
for i in range(N):
    P.append(list(map(int, input().split())))

A = []
def dfs(arr):
    if len(arr) == 10:
        if arr != [0,0,0,0,0,0,0,0,0,0]:
            A.append(arr)
        return
    for i in [0,1]:
        dfs(arr + [i])
dfs([])

ans = -(10**18)
# 10^3 * 10^2 = O(10^5)
for i in range(len(A)):
    tmp = 0
    for j in range(N):
        fac = A[i][0]*F[j][0] + A[i][1]*F[j][1] + A[i][2]*F[j][2] + A[i][3]*F[j][3] + A[i][4]*F[j][4] + A[i][5]*F[j][5] + A[i][6]*F[j][6] + A[i][7]*F[j][7] + A[i][8]*F[j][8] + A[i][9]*F[j][9]
        tmp += P[j][fac]
    ans = max(tmp, ans)
print(ans)