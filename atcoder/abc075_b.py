# 3 5
# .....
# .#.#.
# .....

matrix = []
H, W = map(int, input().split())
for h in range(H):
    matrix.append(list(input()))

for i in range(H):
    for j in range(W):
        if matrix[i][j] == '#': continue
        cnt = 0
        if H > i - 1 >= 0 and W > j - 1 >= 0:
            if matrix[i - 1][j - 1] == '#':
                cnt += 1
        if H > i - 1 >= 0 and W > j >= 0:
            if matrix[i - 1][j] == '#':
                cnt += 1
        if H > i - 1 >= 0 and W > j + 1 >= 0:
            if matrix[i - 1][j + 1] == '#':
                cnt += 1
        if H > i >= 0 and W > j - 1 >= 0:
            if matrix[i][j - 1] == '#':
                cnt += 1
        if H > i >= 0 and W > j + 1 >= 0:
            if matrix[i][j + 1] == '#':
                cnt += 1
        if H > i + 1 >= 0 and W > j - 1 >= 0:
            if matrix[i + 1][j - 1] == '#':
                cnt += 1
        if H > i + 1 >= 0 and W > j >= 0:
            if matrix[i + 1][j] == '#':
                cnt += 1
        if H > i + 1 >= 0 and W > j + 1 >= 0:
            if matrix[i + 1][j + 1] == '#':
                cnt += 1
        matrix[i][j] = cnt

for h in range(H):
    r = ''
    for w in range(W):
        r += str(matrix[h][w])
    print(r)