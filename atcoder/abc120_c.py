S = list(input())
x = 0
y = 0
for i in range(len(S)):
    if S[i] == "0": x += 1
    if S[i] == "1": y += 1
m = min(x,y)
print(2 * m)
