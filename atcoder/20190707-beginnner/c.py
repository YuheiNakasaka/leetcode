L, R = map(int, input().split())
mn = 0
res = 2*(10**9)
i = L
j = L + 1
while i < R:
  mn = (i * j) % 2019
  if mn < res:
      res = mn
  j += 1
  print(i, j, mn)
  if j > R:
      i += 1
      j = i + 1
print(res)