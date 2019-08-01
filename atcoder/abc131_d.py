N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x:x[1])

isYes = True
totalA = 0
for i in range(N):
    totalA += arr[i][0]
    if totalA > arr[i][1]:
        isYes = False

if isYes:
    print('Yes')
else:
    print('No')