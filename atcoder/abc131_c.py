import math
A,B,C,D = list(map(int, input().split()))

# ユークリッドの互除法で最大公約数を計算
# 最大公倍数cd = C * D / 最大公約数
# をmathを使わず計算する
cd = int((C * D) / math.gcd(C, D))

bc = B // C
bd = B // D
bcd = B // cd
ac = (A - 1) // C
ad = (A - 1) // D
acd = (A - 1) // cd

bdiv = bc + bd - bcd
adiv = ac + ad - acd

alldiv = bdiv - adiv

ans = B - A + 1 - alldiv

print(int(ans))
