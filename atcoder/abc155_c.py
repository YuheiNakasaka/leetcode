N = int(input())
S = {}
for i in range(N):
    s = input()
    S[s] = S.get(s, 0) + 1

keys = list(S.keys())
keys.sort(key=lambda x: -S[x])

top_mode = S[keys[0]]

ans = []
for i in range(len(keys)):
    if top_mode == S[keys[i]]:
        ans.append(keys[i])

ans.sort()
for i in range(len(ans)):
    print(ans[i])
