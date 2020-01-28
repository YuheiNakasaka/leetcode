N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

H.sort(key=lambda x: -x)

c = min(K, N)

i = 0
while 0 < c:
    H[i] = 0
    c -= 1
    i += 1

ans = 0
for j in range(i, N):
    ans += H[j]

print(ans)
