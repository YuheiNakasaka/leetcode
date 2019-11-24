A,B,X = list(map(int, input().split()))

if A * (10**9) + B * len(str(10**9)) <= X:
    print(10**9)
else:
    left = 0
    right = 10 ** 9
    mid = 0
    while left < right:
        mid = (left + right) // 2
        x = A * mid + B * len(str(mid))
        if x <= X:
            break
        elif x > X:
            right = mid
        else:
            break

    while True:
        x = A * mid + B * len(str(mid))
        if x >= X:
            break
        mid += 1

    if mid > 0:
        print(min(mid-1, 10**9))
    else:
        print(0)