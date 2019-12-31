N = int(input())
arr = []
for i in range(N-1):
    c, s, f = list(map(int, input().split()))
    arr.append([c, s, f])

ans = []
for i in range(N-1):
    time = arr[i][1]
    for j in range(i, N-1):
        if time > arr[j][1]:
            if time % arr[j][2] != 0:
                time = time + arr[j][2] - (time % arr[j][2]) + arr[j][0]
            else:
                time = arr[j][0] + time
        else:
            time += arr[j][1] - time
            time += arr[j][0]
    print(time)
print(0)