c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))
C = [c1, c2, c3]

# a1を任意に決めるとなし崩し的にa,bが全て出るのであとは全マスでうまくいくか確かめるだけ
f = False
for i in range(C[0][0] + 1):
    a1 = i
    b1 = C[0][0] - a1
    b2 = C[0][1] - a1
    b3 = C[0][2] - a1
    a2 = C[1][0] - b1
    a3 = C[2][0] - b1
    if a1 + b1 == C[0][0] and a1 + b2 == C[0][1] and a1 + b3 == C[0][2] and a2 + b1 == C[1][0] and a2 + b2 == C[1][1] and a2 + b3 == C[1][2] and a3 + b1 == C[2][0] and a3 + b2 == C[2][1] and a3 + b3 == C[2][2]:
        f = True
        break

if f == True:
    print('Yes')
else:
    print('No')