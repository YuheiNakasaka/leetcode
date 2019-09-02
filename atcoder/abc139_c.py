N = int(input())
h = list(map(int, input().split()))

curr = -1
s = 0
ss = [0 for i in range(N)]
for i in range(N-1):
    if h[i] >= h[i+1]:
        ss[i+1] = ss[i] + 1
    else:
        ss[i+1] = 0

print(max(ss))