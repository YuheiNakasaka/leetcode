# 2
# 2
# 2
# 100

# 2

A = int(input())
B = int(input())
C = int(input())
X = int(input())

res = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            total = 500 * a + 100 * b + 50 * c
            if total == X:
                res += 1
print(res)