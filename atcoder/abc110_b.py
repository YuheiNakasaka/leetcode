N,M,X,Y = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.sort(key=lambda x: -x)
y.sort()
left = x[0]
right = y[0]

if left < right:
    flag = False
    while left != right:
        left = left + 1
        if X < left and left < Y and left <= right:
            flag = True
            break
    print('No War') if flag else print('War')
else:
    print('War')