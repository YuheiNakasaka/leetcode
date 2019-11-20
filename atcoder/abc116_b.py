s = int(input())

def even(n):
    return n // 2

def odd(n):
    return 3 * n + 1

l = [0 for _ in range(100000+10)]
a = s
ans = 1
l[a] += 1
while True:
    if a % 2 == 0:
        a = even(a)
    else:
        a = odd(a)
    l[a] += 1
    ans += 1
    if l[a] >= 2:
        break
print(ans)