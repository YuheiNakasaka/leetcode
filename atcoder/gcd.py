# 最大公約数を求めるやつ
def gcd(x, y):
  if y == 0: return x
  return gcd(y, x%y)
