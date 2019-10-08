# S,Tのアルファベットが一対一で痴漢出来れば良い
import sys 
stdin = sys.stdin
ns = lambda : stdin.readline().rstrip()
 
s = ns()
t = ns()

s_cnt = []
t_cnt = []

for alp in "abcdefghijklmnopqrstuvwxyz":
  s_cnt.append(s.count(alp))
  t_cnt.append(t.count(alp))

s_cnt.sort()
t_cnt.sort()

if s_cnt == t_cnt:
  print("Yes")
else:
  print("No")