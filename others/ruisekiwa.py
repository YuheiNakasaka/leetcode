# 累積和
# a(n)は何かしらの数列
# S(n+1) = S(n) + a(n)
# 例題: a(n)の3から5個目までの和を求めよ
# S(5) = a(1) + a(2) + a(3) + a(4) + a(5)
# S(2) = a(1) + a(2)
# S(3, 5) = S(5) - S(2)
a = list(range(1, 6))
S = [0]

for i in range(len(a)):
    S.append(S[i] + a[i])

print('a', a)
print('S', S)
print(S[5] - S[2])