# それぞれ数値anの個数cnを数え上げて
# 多い場合はans1=cn - an
# 少ない場合はans2=cn
# 答えはans1 + ans2
N = int(input())
a = list(map(int, input().split()))
h = {}
for i in range(N):
    h[a[i]] = h.get(a[i], 0)
    h[a[i]] += 1

ans = 0
keys = list(h.keys())
for i in range(len(keys)):
    k = keys[i]
    if k < h[k]:
        ans += h[k] - k
    elif k > h[k]:
        ans += h[k]
print(ans)