from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
N = int(input())
a = list(map(int, input().split()))
a = sorted(a)

a1 = a.pop(0)
a2 = a.pop(0)
res = Decimal((a1 + a2) / 2)

for i in range(N - 2):
    res = Decimal((a[i] + res) / 2)

print(res)