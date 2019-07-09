# 20 2 5

# 84

N, A, B = map(int, input().split())

res = 0
for i in range(1, N+1):
    n = i
    sums = 0
    while i > 0:
      sums += i % 10
      i = int(i / 10)

    if A <= sums and sums <= B:
        res += n

print(res)