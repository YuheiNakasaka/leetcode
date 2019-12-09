S = list(input())

ans = 0
if len(S) % 2 == 0:
    l = S[:len(S) // 2]
    r = list(reversed(S[len(S) // 2:]))
    for i in range(len(l)):
        if l[i] != r[i]:
            ans += 1
else:
    l = S[:len(S) // 2]
    r = list(reversed(S[(len(S) // 2)+1:]))
    for i in range(len(l)):
        if l[i] != r[i]:
            ans += 1

print(ans)