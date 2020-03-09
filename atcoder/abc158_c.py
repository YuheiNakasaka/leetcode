import math
from decimal import *
A,B = list(map(int, input().split()))
ans = -1
for x in range(1, 10001):
    a = math.floor(x * Decimal(0.08))
    b = math.floor(x * Decimal(0.1))
    if a == A and b == B:
        ans = x
        break
print(ans)