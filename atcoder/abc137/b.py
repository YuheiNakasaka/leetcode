K, X = list(map(int, input().split()))

right = X + K
left = X - K + 1

l = list(range(left, X))
r = list(range(X, right))

print(" ".join(map(str, l + r)))
