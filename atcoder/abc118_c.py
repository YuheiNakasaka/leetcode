import sys
readline = sys.stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a.sort()

zero_count = 0
curr = 0
i = 0

while n - zero_count > 1:
    # print(i,curr,zero_count,a)
    if i != curr and a[i] != 0:
        if a[i] % a[curr] == 0:
            a[i] = 0
        elif a[curr] <= a[i]:
            a[i] = a[i] % a[curr]
            if a[i] < a[curr]:
                curr = i
        if a[i] == 0:
            zero_count += 1
    if i == n - 1:
      i = 0
    else:
      i += 1

print(max(a))