n = int(input())
b = list(map(int, input().split()))

a = [0 for _ in range(n)]

a[0] = b[0]
a[-1] = b[-1]
for i in range(n - 2):
    ai_1 = min(b[i],b[i+1])
    a[i+1] = ai_1

print(sum(a))