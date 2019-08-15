H, W = list(map(int, input().split()))
s = []
for i in range(H):
    s.append(list(input()))

wblock = []
hblock = []

for y in range(H):
    for x in range(W):
        if s[y][x] == '#':
            wblock.append([y,x])

for x in range(W):
    for y in range(H):
        if s[y][x] == '#':
            hblock.append([y, x])

print(wblock, hblock)