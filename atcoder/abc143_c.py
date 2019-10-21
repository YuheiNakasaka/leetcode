N = int(input())
S = list(input())

ch = ''
ans = 0
for i in range(N):
    if S[i] != ch:
        ch = S[i]
        ans += 1

print(ans)