# 9 45000
# 4 0 5

# 20 196000
# -1 -1 -1

# 1000 1234000
# 14 27 959

# 2000 20000000
# 2000 0 0

N, Y = map(int, input().split())
X_yen = 10000
Y_yen = 5000
Z_yen = 1000
x = y = z = -1
for a in range(N + 1):
    for b in range(N + 1 - a):
        c = N - a - b
        total = 10000*a + 5000*b + 1000*c
        if total == Y:
            x = a
            y = b
            z = c
print(x, y, z)