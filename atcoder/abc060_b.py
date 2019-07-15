A, B, C = map(int, input().split())

res = False
a = A
while a < B * A:
    if a % B == C:
        res = True
        break
    a += A

print('YES') if res else print('NO')