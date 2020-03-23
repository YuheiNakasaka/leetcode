from decimal import Decimal
L = int(input())

l = Decimal(L) / Decimal(3)

print(Decimal(l) * Decimal(l) * Decimal(l))