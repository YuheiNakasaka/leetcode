A = list(map(int, input().split()))

resp = A[0] + A[1] + A[2]

if resp >= 22:
    print('bust')
else:
    print('win')