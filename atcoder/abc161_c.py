N, K = list(map(int, input().split()))

t = N % K
k = K - t

print(min(t, k))