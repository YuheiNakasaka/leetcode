import statistics

N = int(input())
A = list(map(int, input().split()))

t = []
for i in range(N):
    t.append(A[i] - i)

if len(A) % 2 == 1:
    b = statistics.median(t)
    ans = 0
    for i in range(N):
        ans += abs(A[i] - i - b)
    print(ans)
else:
    t.sort()
    b1 = t[len(t) // 2]
    b2 = t[(len(t) // 2) - 1]
    ans1 = 0
    ans2 = 0
    for i in range(N):
        ans1 += abs(A[i] - i - b1)
    for i in range(N):
        ans2 += abs(A[i] - i - b2)
    print(min(ans1, ans2))