A, B, C = list(map(int, input().split()))
res = C - (A - B)

if res <= 0:
    print(0)
else:
    print(res)
