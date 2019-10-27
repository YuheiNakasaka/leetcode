# 死んだ
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
F = list(map(int, input().split()))

# if sum(A) <= K:
#     print(0)
# else:
#     A.sort(key=lambda x: -x)
#     F.sort(key=lambda x: -x)
#     m = 0
#     for i in range(N):
#         if K > 0:
#             if K > A[i]:
#                 d = K - A[i]
#                 A[i] = max(A[i] - K, 0)
#                 K = d
#             else:
#                 A[i] -= K
#                 K = 0
#                 m = i
#         else:
#             break
#     if m + 1 < N:
#         print(max(A[m] * F[m], A[m+1]*F[m+1]))
#     else:
#         print(A[m]*F[m])
