S = input()
K = int(input())
N = len(S)

# うまいこと全列挙のする方法がわからなかったがこうやれば良いのか...
tmp = set()
for i in range(min(N,K)):
    for j in range(N-i):
        tmp.add(S[j:j+i+1])

tmp = list(tmp)
tmp.sort()
print(tmp[K-1])