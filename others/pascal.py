N = 100
arr = [[1]]
for i in range(N):
    if i != 0: arr.append([1] * (i+1))
    for j in range(i):
        if j == 0:
            arr[i][j] = 1
        elif j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(len(arr)):
    print(arr[i])