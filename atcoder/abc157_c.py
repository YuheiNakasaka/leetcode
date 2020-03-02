N, M = list(map(int, input().split()))
s = []
c = []
for _ in range(M):
    _s, _c = list(map(int, input().split()))
    s.append(_s)
    c.append(_c)

if N == 1:
    ans = [0]
else:
    ans = [1]
    ans = ans + [0 for _ in range(N - 1)]

flag = True
dup = [-1 for _ in range(N)]
for i in range(M):
    idx = s[i] - 1
    if N > 1 and s[i] == 1 and c[i] == 0:
        flag = False
        break
    if dup[idx] != -1 and ans[idx] != c[i]:
        flag = False
        break
    ans[idx] = c[i]
    dup[idx] = 1

if flag == False:
    print(-1)
else:
    print(''.join(map(str, ans)))