S = [int(s) for s in list(input())]
K = int(input())

first_char = S[0]
if len(S) == 1:
    print(first_char)
elif first_char == 1:
    cnt = 0
    prev = 1
    i = 0
    while i < len(S) and prev == S[i]:
        prev = S[i]
        i += 1
    if K <= i:
        print(1)
    else:
        print(S[i])
else:
    print(first_char)
