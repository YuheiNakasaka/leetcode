N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

h = {}
for i in range(N):
    b = h.get(a[i], 0)
    h[a[i]] = b + 1

if len(h.keys()) <= K:
    print(0)
else:
    ans = 0
    keys = sorted(h.keys(), key=lambda x: h[x])
    for i in range(len(keys) - K):
        ans += h[keys[i]]
    print(ans)