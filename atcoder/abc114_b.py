S = list(input())
ans = 1000000007
for i in range(len(S) - 2):
    d = int(S[i] + S[i+1] + S[i+2])
    ans = min(abs(d - 753), ans)
print(ans)
