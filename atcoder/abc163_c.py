N = int(input())
A = list(map(int, input().split()))

ah = {}
for i in range(len(A)):
  ah[A[i]] = ah.get(A[i], 0)
  ah[A[i]] += 1

for i in range(N):
  print(ah.get(i+1, 0))
