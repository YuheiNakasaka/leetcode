# (A ~ B までの個数) - (Cで割り切れるもの + Dで割り切れるもの - CDの最小公倍数で割り切れるもの)
A,B,C,D = list(map(int, input().split()))

def euc(a, b):
    a, b = [max(a, b), min(a, b)]
    if b == 0:
        return a
    else:
        return euc(b, a % b)

Cdiv = (B // C) - ((A-1) // C)
Ddiv = (B // D) - ((A-1) // D)
E = (C * D) // euc(C, D)
CDdiv = (B // E) - ((A-1) // E)

print((B - A + 1) - (Cdiv + Ddiv - CDdiv))