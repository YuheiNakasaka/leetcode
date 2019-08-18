from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
N = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(N):
    res += 1 / a[i]

print(Decimal(1/res))
