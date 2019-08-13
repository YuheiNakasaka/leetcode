N, M = list(map(int, input().split(" ")))
a = []
for i in range(M):
    a.append(int(input()))

stairs = [1 for _ in range(N+1)]

for v in a:
    stairs[v] = 0

for i in list(range(0, N - 1))[::-1]:
    if stairs[i] == 0:
        continue
    stairs[i] = (stairs[i+1] + stairs[i+2]) % 1000000007

print(stairs[0])
