H, W = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]

flag = True
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            # 上下左右
            if (i-1 >= 0 and S[i-1][j] == '#') or (i+1 < H and S[i+1][j] == '#') or (j-1 >= 0 and S[i][j-1] == '#') or (j+1 < W and S[i][j+1] == '#'):
                continue
            else:
                flag = False

if flag:
    print('Yes')
else:
    print('No')
