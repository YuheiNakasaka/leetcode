from decimal import Decimal
N = int(input())
X = []
btc_rate = Decimal("380000.0")
for _ in range(N):
    x, u = list(input().split())
    X.append([Decimal(str(x)), u])

ans = 0
for i in range(N):
    amount = X[i][0]
    unit = X[i][1]
    if unit == 'JPY':
        ans += amount
    else:
        ans += btc_rate * amount

print(ans)