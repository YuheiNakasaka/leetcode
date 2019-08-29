N, M = list(map(int, input().split()))
ab = []
for i in range(N):
    A, B = list(map(int, input().split()))
    ab.append([A, B])

ab = sorted(ab, key=lambda x: x[0])

s = 0
for i in range(len(ab)):
    if M - ab[i][1] > 0:
        # print(ab[i][0],ab[i][1],ab[i][0] * ab[i][1],M)
        M -= ab[i][1]
        s += ab[i][0] * ab[i][1]
    else:
        for j in range(ab[i][1]):
            # print(ab[i][0],ab[i][1],ab[i][0] * ab[i][1],M)
            M -= 1
            s += ab[i][0]
            if M == 0:
                break
        break

print(s)