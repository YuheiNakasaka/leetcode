from math import gcd
K = int(input())

ans = 0
h = {}
for i in range(1, K+1):
  for j in range(1, K+1):
    x = gcd(i, j)
    h[x] = h.get(x, 0)
    h[x] += 1

keys = list(h.keys())
n = len(keys)
for i in range(n):
  tmp = 0
  key = keys[i]
  for j in range(1, K+1):
    tmp += gcd(key, j)
  ans += tmp * h[key]

print(ans)