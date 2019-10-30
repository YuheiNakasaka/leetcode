r, D, x = list(map(int, input().split()))

nx = x
for i in range(10):
    nx = r * nx - D
    print(nx)