S = list(input())
T = list(input())

i = len(S) - 1
ti = len(T) - 1
match = 0
ms = len(S) - 1
flag = False
while 0 <= i:
    if S[i] == T[ti] or S[i] == '?':
        if ms == -1:
            ms = i
        match += 1
        ti -= 1
        i -= 1
    else:
        if match > 0:
            match = 0
            ti = len(T) - 1
            i = ms - 1
            ms = -1
        else:
            ms = -1
            match = 0
            ti = len(T) - 1
            i -= 1
    if match == len(T):
        k = 0
        i += 1
        for j in range(i, i + len(T)):
            S[j] = T[k]
            k += 1
        flag = True
        break

# print(S)
# print(T)

if flag == True:
    for i in range(len(S)):
        if S[i] == '?':
            S[i] = 'a'
    print(''.join(S))
else:
    print('UNRESTORABLE')
