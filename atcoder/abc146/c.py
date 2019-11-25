A,B,X = list(map(int, input().split()))

if A * (10**9) + B * len(str(10**9)) <= X:
    print(10**9)
else:
    left = 0
    right = 10 ** 9
    mid = 0
    dup = 0
    prev = 0
    while left != right:
        mid = (left + right) // 2
        x = A * mid + B * len(str(mid))
        if mid == prev:
            dup += 1
        if dup > 10:
            break
        prev = mid
        if x < X:
            left = mid
        elif x > X:
            right = mid
        else:
            break
    print(mid)