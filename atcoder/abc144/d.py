# 死んだ
import math
a, b, x = list(map(int, input().split()))

ans = 0
if a * a *b / 2.0 <= x:
    ans = math.atan(2 * (a * a * b - x) / (a * a * a))
else:
    ans = math.pi / 2 - math.atan(2 * x / (a * b * b))

print(math.degrees(ans))