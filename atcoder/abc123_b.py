arr = []
arr.append(int(input()))
arr.append(int(input()))
arr.append(int(input()))
arr.append(int(input()))
arr.append(int(input()))

y = []
for i in range(len(arr)):
    next_time = ((arr[i] + 10) // 10) * 10
    diff = next_time - arr[i]
    if diff == 10:
        y.append([arr[i], 0])
    else:
        y.append([arr[i], diff])

y.sort(key=lambda x: -x[1])

ans = 0
for i in range(len(y)):
    if i == 0:
        ans += y[i][0]
    else:
        ans += y[i][0] + y[i][1]

print(ans)