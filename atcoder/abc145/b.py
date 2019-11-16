N = int(input())
S = list(input())
if N % 2 == 1:
    print('No')
else:
    mid = N // 2
    left = S[:mid]
    right = S[mid:]
    if left == right:
        print('Yes')
    else:
        print('No')