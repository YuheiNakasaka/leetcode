N = int(input())
S = list(input())

# 左から
l = 0
li = 0
lmax = -(10**8)
for i in range(N):
    if S[i] == 'W':
        l -= 1
    else:
        l += 1
    if l > lmax:
      lmax = l
      li = i

lans = 0
for i in range(N):
    if i < li:
        if S[i] == 'W':
            lans += 1
    if li < i:
        if S[i] == 'E':
            lans += 1

# 右から
r = 0
ri = 0
rmax = -(10**8)
for i in reversed(range(N)):
    if S[i] == 'E':
        r -= 1
    else:
        r += 1
    if r > rmax:
      rmax = r
      ri = i

rans = 0
for i in range(N):
    if i < ri:
        if S[i] == 'W':
            rans += 1
    if ri < i:
        if S[i] == 'E':
            rans += 1

# print(li, ri)
print(min(lans, rans))