# n = int(input())
# a = list(map(int, input().split()))

# たまたま3つごとに処理するパターンがうまくいくだけなのでだめ
# ans = 0
# start = 0
# for i in range(n // 3 + 1):
#     if len(a[start:]) >= 3:
#       i0 = start
#       i1 = start + 1
#       i2 = start + 2
#       # 全てプラス
#       if a[i0] >= 0 and a[i1] >= 0 and a[i2] >= 0:
#           ans += a[i0] + a[i1] + a[i2]
#           continue
#       A = a[i0] + a[i1] + a[i2]
#       B = -1*a[i0] + (-1*a[i1]) + a[i2]
#       C = -1*a[i0] + a[i1] + (-1*a[i2])
#       D = a[i0] + (-1*a[i1]) + (-1*a[i2])
#       print(A,B,C,D)
#       ans += max([A,B,C,D])
#       start = i2 + 1
#     elif len(a[start:]) == 2:
#       i0 = start
#       i1 = start + 1
#       # 全てプラス
#       if a[i0] >= 0 and a[i1] >= 0:
#           ans += a[i0] + a[i1]
#           continue
#       A = a[i0] + a[i1]
#       B = -1*a[i0] + (-1*a[i1])
#       ans += max([A,B])
#     elif len(a[start:]) == 1:
#       # 最後が１個の時は操作ができないのでただ足すだけ
#       ans += a[start]

# print(ans)

# i = 0
# ans = 0
# while i < n:
#     if a[i] >= 0:
#         ans += a[i]
#         i += 1
#         continue
#     if len(a[i:]) == 2:
#         i0 = i
#         i1 = i + 1
#         A = a[i0] + a[i1]
#         B = -1*a[i0] + (-1*a[i1])
#         ans += max([A,B])
#         break
#     if len(a[i:]) == 1:
#         ans += a[i]
#         break

#     if a[i] < 0 and a[i+1] >= 0 and a[i+2] < 0:
#         ans += (-1*a[i]) + a[i+1] + (-1*a[i+2])
#         i += 3
#     else:
#         i0 = i
#         i1 = i + 1
#         i2 = i + 2
#         A = a[i0] + a[i1] + a[i2]
#         B = -1*a[i0] + (-1*a[i1]) + a[i2]
#         C = -1*a[i0] + a[i1] + (-1*a[i2])
#         D = a[i0] + (-1*a[i1]) + (-1*a[i2])
#         ans += max([A,B,C,D])
#         i += 3

# print(ans)

N = int(input())
A = list(map(int, input().split()))
 
cnt = 0 # -の個数
minus = 10**9 # 絶対値が最小の数を入れる
ans = 0
 
for i in range(N):
    if A[i] < 0:
        cnt += 1
        minus = min(minus, -A[i])
        ans += -A[i]
    else:
        minus = min(minus, A[i])
        ans += A[i]
 
if cnt % 2 == 0:
    print(ans)
else:
    print(ans - minus * 2)