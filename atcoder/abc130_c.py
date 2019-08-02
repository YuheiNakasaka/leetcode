W, H, x, y = list(map(int, input().split()))
square = (W * H) / 2
cnt = '0'
if x + x == W and y + y == H:
    cnt = '1'
print(square, cnt)