N, D = map(int, input().split())

i = 1
left = 1
res = 0
while i <= N:
    if i - D == left:
        left = i + D + 1
        res += 1
    i += 1

if left <= N: res += 1

print(res)