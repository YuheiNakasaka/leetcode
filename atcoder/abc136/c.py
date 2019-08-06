N = int(input())
H = list(map(int, input().split()))

res = 'Yes'
maximum = 0
for i in range(N - 1):
    if maximum < H[i]:
        maximum = H[i]
    if maximum - H[i+1] >= 2:
        res = 'No'

print(res)