# だめ
S = input()
N = len(S)
s = list(S)

res = [0]*N
for i in range(N):
    step = 0
    firstCh = s[i]
    if i == N -1:
        for j in range(1, N - i):
            step += 1
            if s[i+j] != firstCh:
                break
    else:
        for j in range(1, N - i + 1):
            step += 1
            if s[i+j] != firstCh:
                break

    if step % 2 == 0:
        res[i + step] += 1
    else:
        res[i + step - 1] += 1

print(res)
