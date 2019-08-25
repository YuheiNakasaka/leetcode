N = list(input())

ans1 = 0
expected = N[0]
for n in N[1:]:
    if expected == n:
        ans1 += 1
        if n == '0':
            expected = '1'
        else:
            expected = '0'
    else:
        expected = n

N.reverse()
ans2 = 0
expected = N[0]
for n in N[1:]:
    if expected == n:
        ans2 += 1
        if n == '0':
            expected = '1'
        else:
            expected = '0'
    else:
        expected = n


print(min(ans1, ans2))