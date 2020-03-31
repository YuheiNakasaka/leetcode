K, N = list(map(int, input().split()))
A = list(map(int, input().split()))

s = []
for i in range(N):
  if N == i + 1:
    s.append(A[0] + abs(K - A[i]))
  else:
    s.append(abs(A[i+1] - A[i]))

total = 0
srtd = sorted(s)
for i in range(len(srtd) - 1):
  total += srtd[i]

print(total)