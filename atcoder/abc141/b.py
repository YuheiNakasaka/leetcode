S = input()
flag = True
for i in range(len(S)):
    s = S[i]
    if (i + 1) % 2 == 0: # 偶数
        if s != 'L' and s != 'U' and s != 'D':
            flag = False
            break
    else: # 奇数
        if s != 'R' and s != 'U' and s != 'D':
            flag = False
            break

if flag == False:
    print('No')
else:
    print('Yes')