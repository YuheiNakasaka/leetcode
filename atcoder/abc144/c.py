import math
N = int(input())

lim = int(math.sqrt(N))

x = 1
while True:
    if N % lim == 0:
        x = lim
        break
    lim = lim - 1

y = N // lim

print((x - 1) + (y - 1))