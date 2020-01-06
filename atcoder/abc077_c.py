import bisect
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    l = bisect.bisect_left(A, B[i])
    r = N - bisect.bisect_right(C, B[i])
    ans += l * r

print(ans)