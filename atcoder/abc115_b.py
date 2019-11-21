N = int(input())
p = []
for _ in range(N):
    p.append(int(input()))
p.sort(key=lambda x: -x)
print(p[0] // 2 + sum(p[1:]))
