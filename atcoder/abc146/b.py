N = int(input())
S = list(input())
a = [chr(i) for i in range(65, 65+26)]

for i in range(len(S)):
    current_i = a.index(S[i])
    next_i = (current_i + N) % 26
    S[i] = a[next_i]

print(''.join(S))