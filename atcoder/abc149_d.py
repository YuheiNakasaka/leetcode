N,K = list(map(int, input().split()))
R,S,P = list(map(int, input().split()))
T = list(input())

ans = 0
for i in range(K):
    scorer = 0
    prev = ''
    for j in range(i, N, K):
        if T[j] == "r":
            if prev != 'p':
                scorer += P
                prev = 'p'
            else:
                prev = ''
        elif T[j] == "s":
            if prev != 'r':
                scorer += R
                prev = 'r'
            else:
                prev = ''
        elif T[j] == "p":
            if prev != 's':
                scorer += S
                prev = 's'
            else:
                prev = ''
    ans += scorer

print(ans)