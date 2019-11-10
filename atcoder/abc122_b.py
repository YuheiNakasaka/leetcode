S = list(input())

ans = 0
cnt = 0
i = 0
while i < len(S):
    first = S[i]
    if first == 'A' or first == 'C' or first == 'G' or first == 'T':
        cnt += 1
        ans = max(ans, cnt)
    else:
        ans = max(ans, cnt)
        cnt = 0
    i += 1
print(ans)