N, X = list(map(int, input().split()))
L = list(map(int, input().split()))
L = [0] + L
step = 0
total = 0
for l in range(N + 1):
    step += L[l]
    if step <= X:
        total += 1
print(total)