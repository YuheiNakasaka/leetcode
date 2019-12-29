N = int(input())
A1 = [0] + list(map(int, input().split()))
A2 = [0] + list(map(int, input().split()))

R1 = [0] + [0 for _ in range(N)]
R2 = [0] + [0 for _ in range(N)]
for i in range(1, N+1):
    R1[i] = R1[i - 1] + A1[i]
    R2[i] = R2[i - 1] + A2[i]

# print(R1,R2)

ans = 0
for i in range(1, N+1):
    ans = max(R1[i] + (R2[N] - R2[i - 1]), ans)

print(ans)