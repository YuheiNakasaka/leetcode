N,A,B = list(map(int, input().split()))
train = A * N
taxi = B
if train < taxi:
    print(train)
else:
    print(taxi)