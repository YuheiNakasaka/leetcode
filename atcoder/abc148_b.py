N = int(input())
S, T = list(input().split())

ans = ''
i = 0
while i < N:
    ans += S[i]
    ans += T[i]
    i += 1
print(ans)