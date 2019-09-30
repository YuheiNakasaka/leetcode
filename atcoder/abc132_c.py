N = int(input())
d = list(map(int, input().split()))

d.sort()

center = N // 2

L = d[:center]
R = d[center:]

# print(L,R)

ans = R[0] - L[-1]

print(ans)