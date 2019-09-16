# # 2より大きい値段のものに高いものから順に割引券を振り分けていく
# n,m = list(map(int, input().split()))
# a = list(map(int, input().split()))
# a = sorted(a, key=lambda x: -x)
# coupon = [0 for i in range(n)]

# v = 0
# for i in range(n):
#     if a[i] > 2:
#         v += 1

# i = 0
# while m > 0 and v > 0:
#     if len(a) == 1:
#         coupon[i] = m
#         break
#     if a[i] > 2:
#         l = a[i] // 2**(coupon[i]+1)
#         if l >= 0:
#             coupon[i] += 1
#             if l == 0:
#                 v -= 1
#         m -= 1
#         i += 1
#     elif a[i] <= 2 and m > 0:
#         i = 0

# total = 0
# for i in range(n):
#     if a[i] < 3 and m > 0:
#       total += a[i] // 2
#       m -= 1
#     else:
#       total += a[i] // 2**coupon[i]

# print(total)

import heapq
n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = []
for i in range(n):
    heapq.heappush(b, a[i] * (-1))

while m > 0:
    bb = ((heapq.heappop(b) * (-1)) // 2) * (-1)
    heapq.heappush(b, bb)
    m -= 1

total = 0
for i in range(n):
    total += b[i] * -1

print(total)