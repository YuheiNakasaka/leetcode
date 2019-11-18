A,B,K = list(map(int, input().split()))

Al = []
Bl = []

for i in range(1, A + 1):
    if A % i == 0:
        Al.append(i)

for i in range(1, B + 1):
    if B % i == 0:
        Bl.append(i)

ABl = []
for i in range(len(Al)):
    for j in range(len(Bl)):
        if Al[i] == Bl[j]:
            ABl.append(Al[i])

ABl.sort(key=lambda x: -x)

print(ABl[K - 1])