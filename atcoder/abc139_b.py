A, B = list(map(int, input().split()))
if B == 1: 
  print('0')
else:
  s = 0
  ans = 0
  while s < B:
      s += A
      ans += 1
      if s < B:
          s -= 1
  print(ans)