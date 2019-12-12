S = list(input())

prev = S[0]
flag = True
for i in range(1, 4):
    if prev == S[i]:
        flag = False
        break
    prev = S[i]

if flag:
    print('Good')
else:
    print('Bad')