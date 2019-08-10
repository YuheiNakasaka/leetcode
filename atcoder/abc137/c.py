def cmb(n, r):
  if n - r < r: r = n - r
  if r == 0: return 1
  if r == 1: return n

  numerator = [n - r + k + 1 for k in range(r)]
  denominator = [k + 1 for k in range(r)]

  for p in range(2,r+1):
      pivot = denominator[p - 1]
      if pivot > 1:
          offset = (n - r) % p
          for k in range(p-1,r,p):
              numerator[k - offset] /= pivot
              denominator[k] /= pivot

  result = 1
  for k in range(r):
      if numerator[k] > 1:
          result *= int(numerator[k])

  return result

N = int(input())
s = {}
h = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e':11, 'f':13, 'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,'n':43,'o':47,'p':53,'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,'y':97,'z':101}
for i in range(N):
    total = 1
    chs = list(input())
    for j in range(10):
        total *= h[chs[j]]
    s[total] = s.get(total, 0) + 1

cnt = 0
for v in s.values():
    if v < 2: continue
    a = cmb(v, 2)
    cnt += a

print(int(cnt))