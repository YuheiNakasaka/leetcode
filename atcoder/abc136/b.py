N = int(input())

resp = 0
if N < 10:
    resp = N
elif 10 <= N < 100:
    resp = 9
elif 100 <= N < 1000:
    a = 9
    b = N - 99
    resp = a + b
elif 1000 <= N < 10000:
    resp = 9 + (999 - 99)
elif 10000 <= N < 100000:
    a = 9
    b = 999 - 99
    c = N - 9999
    resp = a + b + c
elif 100000 <= N:
    resp = 90909

print(resp)