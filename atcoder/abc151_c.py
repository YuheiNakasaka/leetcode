N,M = list(map(int, input().split()))
ps = []
for i in range(M):
    p, s = input().split()
    ps.append([int(p), s])

ac = {}
wa = {}
for i in range(M):
    if ps[i][1] == 'AC':
        if not ac.get(ps[i][0]):
            ac[ps[i][0]] = 1
    else:
        if not ac.get(ps[i][0]):
            wa[ps[i][0]] = wa.get(ps[i][0], 0)
            wa[ps[i][0]] += 1

ansac = len(ac.keys())
answa = 0
for k in wa.keys():
    if ac.get(k):
        answa += wa[k]

print(ansac, answa)