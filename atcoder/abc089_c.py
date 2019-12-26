N = int(input())
inis = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for i in range(N):
    s = list(input())
    if s[0] == "M" or s[0] == "A" or s[0] == "R" or s[0] == "C" or s[0] == "H":
        inis[s[0]] += 1

ans = 0
march = ["M","A","R","C","H"]
for i in range(len(march)):
    for j in range(i, len(march)):
        for k in range(j, len(march)):
            if march[i] != march[j] and march[i] != march[k] and march[j] != march[k]:
                ans += inis[march[i]] * inis[march[j]] * inis[march[k]]

print(ans)