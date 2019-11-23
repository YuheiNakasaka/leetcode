n = int(input())
u = list(map(int, input().split()))
A = []
B = []
Af = [[i, -1] for i in range(100007)]
Bf = [[i, -1] for i in range(100007)]
for i in range(n):
    if i % 2 == 0:
        A.append(u[i])
        Af[u[i]][1] += 1
    else:
        B.append(u[i])
        Bf[u[i]][1] += 1

Af.sort(key=lambda x: -x[1])
Bf.sort(key=lambda x: -x[1])

Ae = 0
Be = 0
ans = 0
if Af[0][0] == Bf[0][0]:
    Ae = Af[0][0]
    Be = Bf[1][0]
    ans1 = 0
    for i in range(len(A)):
        if Ae != A[i]:
            ans1 += 1
    for i in range(len(B)):
        if Be != B[i]:
            ans1 += 1

    Ae = Af[1][0]
    Be = Bf[0][0]
    ans2 = 0
    for i in range(len(A)):
        if Ae != A[i]:
            ans2 += 1
    for i in range(len(B)):
        if Be != B[i]:
            ans2 += 1
    ans = min(ans1, ans2)
else:
    Ae = Af[0][0]
    Be = Bf[0][0]
    for i in range(len(A)):
        if Ae != A[i]:
            ans += 1
    for i in range(len(B)):
        if Be != B[i]:
            ans += 1

print(ans)