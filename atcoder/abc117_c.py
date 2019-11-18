N, M = list(map(int, input().split()))
X = list(map(int, input().split()))
if N >= M:
    print(0)
else:
    X.sort()
    diff = []
    for i in range(M - 1):
        diff.append(abs(X[i + 1] - X[i]))
    diff.sort()
    print(sum(diff[:len(diff) - (N - 1)]))