# 4 2 9

N, A, B = map(int, input().split())

bus_fare = N * A

if bus_fare > B:
    print(B)
else:
    print(bus_fare)

