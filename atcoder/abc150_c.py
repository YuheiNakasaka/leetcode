import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

a = 0
b = 0
i = 1

for x in itertools.permutations(list(range(1,N+1))):
    l = list(x)
    if P == l:
        a = i
    if Q == l:
        b = i
    i += 1

print(abs(a - b))