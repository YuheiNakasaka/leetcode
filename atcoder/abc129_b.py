N = int(input())
W = list(map(int, input().split()))
A = sum(W)
S1 = 0
ans = 10**9
for i in range(N):
    S1 += W[i]
    S2 = A - S1
    diff = abs(S1 - S2)
    if ans > diff:
        ans = diff
print(ans)