A, B = map(int, input().split())
res = (A + B) / 2
if res.is_integer():
    print(int(res))
else:
    print('IMPOSSIBLE')