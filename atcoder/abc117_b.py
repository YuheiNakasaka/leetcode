N = int(input())
L = list(map(int, input().split()))

L.sort(key=lambda x: -x)

if L[0] < sum(L[1:]):
    print('Yes')
else:
    print('No')