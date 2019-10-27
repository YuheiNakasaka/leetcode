N, L = list(map(int, input().split()))

aji = []
for i in range(1, N + 1):
    aji.append(L + i - 1)

a = sum(aji)

ans = 0
diff = 10**9
for i in range(N):
    s = sum(aji) - aji[i]
    t = abs(a - s)
    if t < diff:
      diff = t
      ans = s

print(ans)