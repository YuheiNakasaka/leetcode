N, X = list(map(int, input().split()))
x = list(map(int, input().split()))

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

m = []
for i in range(N):
    m.append(abs(X - x[i]))

c = m[0]
for i in range(1, N):
    if c == 1: break
    c = gcd(c, m[i])

print(c)