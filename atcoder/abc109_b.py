N = int(input())
words = []
for i in range(N):
    w = list(input())
    words.append(w)
h = {}
p = words[0][0]
f = True
for i in range(N):
    b = words[i][0]
    l = words[i][-1]
    if b != p:
        f = False
        break
    p = l
    if h.get(''.join(words[i])) != None:
        f = False
        break
    h[''.join(words[i])] = 1

if f == True:
    print('Yes')
else:
    print('No')