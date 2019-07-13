import math

N = int(input())

num = 1
for i in range(1, N+1):
    num = i * num % (10**9 + 7)
    print(num)

print(num)

# 別解: math.factorialを使うと階乗計算がクソ速い
# print(math.factorial(N) % (10**9 + 7))