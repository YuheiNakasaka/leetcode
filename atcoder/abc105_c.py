import sys
from collections import deque

N = int(input())

ans = deque([])
if N == 0:
    print(0)
else:
    while N != 0:
        if N % -2 != 0:
            N -= 1
            ans.appendleft('1')
        else:
            ans.appendleft('0')
        N /= -2
    print(''.join(ans))
