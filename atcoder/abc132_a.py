S = list(input())
h = {}
for s in S:
    h[s] = 1
if len(h.keys()) == 2:
    print('Yes')
else:
    print('No')