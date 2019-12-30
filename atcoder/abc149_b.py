a, b, k = list(map(int, input().split()))
ka = k - a
if ka <= 0:
    print('%d %d' % (a - k, b))
else:
    if b < ka:
        ka = b
    print('0 %d' % (b - ka))