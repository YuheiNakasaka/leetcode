A, B, C, D, E, F = list(map(int, input().split()))

sw = 100 * A
sugar = 0
percent = 0
for k in range(F // (100 * A) + 1):
    for l in range(F // (100 * B) + 1):
        if k == 0 and l == 0:
            continue
        tmp = A * k + B * l
        if 100 * tmp > F:
            continue
        for i in range(tmp*E//C + 1):
            for j in range(tmp*E//D + 1):
                tmp2 = i * C + j * D
                if 100 * tmp + tmp2 > F:
                    continue
                if tmp2 > tmp * E:
                    continue
                t = 100 * tmp2 / (100 * tmp + tmp2)
                if t > percent:
                    percent = t
                    sw = 100 * tmp + tmp2
                    sugar = tmp2

print(sw, sugar)