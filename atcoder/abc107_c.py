N, K = list(map(int, input().split()))
X = list(map(int, input().split()))

X.sort()

ma = max(X)
mi = min(X)

if ma <= 0:
    X.sort(key=lambda x: -x)
    a = 0
    for i in range(K):
        a = X[i]
    print(abs(a))
elif 0 <= mi:
    a = 0
    for i in range(K):
        a = X[i]
    print(abs(a))
else:
    ans = 1000000000000000000
    for i in range(N):
        l = i
        r = i + K - 1
        if r < N and X[l] <= 0 <= X[r]:
            if abs(X[l]) > abs(X[r]):
                ans = min(abs(X[r]) * 2 + abs(X[l]), ans)
            else:
                ans = min(abs(X[l]) * 2 + abs(X[r]), ans)
    print(ans)

    
