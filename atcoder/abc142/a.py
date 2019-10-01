import sys
readline = sys.stdin.readline

N = int(readline())


if N % 2 == 0:
  print((N//2) / N)
else:
  print(((N//2)+1) / N)
