import copy
N = int(input())
p = list(map(int, input().split()))

is_asc = True

for k in range(N-1):
  if p[k] > p[k+1]: is_asc = False

if is_asc == True:
    print('YES')
else:
  for i in range(N):
      for j in range(N):
          if i == j: continue
          is_asc = True
          tmp_p = copy.deepcopy(p)
          tmp = p[i]
          tmp_p[i] = p[j]
          tmp_p[j] = tmp
          for k in range(N-1):
              if tmp_p[k] > tmp_p[k+1]: is_asc = False
          if is_asc == True:
              break
      if is_asc == True:
          break

  if is_asc == True:
      print('YES')
  else:
      print('NO')