A,B = list(map(int, input().split()))

c = A - (B * 2)
if c >= 0:
    print(c)
else:
    print(0)