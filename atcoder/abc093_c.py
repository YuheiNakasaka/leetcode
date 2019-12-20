# A,B,C=(偶,偶,偶),(奇,奇,奇)なら2を足すだけで良い
#(偶,奇,奇)(偶,偶,奇)は偶偶,奇奇をそれぞれ反転させてあとは２を足す
A,B,C = list(map(int, input().split()))

a = A % 2
b = B % 2
c = C % 2

ans = 0
if (a == 0 and b == 0 and c == 1):
    A += 1
    B += 1
    ans += 1
elif (a == 0 and b == 1 and c == 0):
    A += 1
    C += 1
    ans += 1
elif (a == 1 and b == 0 and c == 0):
    B += 1
    C += 1
    ans += 1
elif (a == 1 and b == 0 and c == 1):
    A += 1
    C += 1
    ans += 1
elif (a == 1 and b == 1 and c == 0):
    A += 1
    B += 1
    ans += 1
elif (a == 0 and b == 1 and c == 1):
    B += 1
    C += 1
    ans += 1

arr = sorted([A,B,C])
l = arr[2]
m = arr[1]
n = arr[0]
ans += (l - m) // 2
ans += (l - n) // 2
print(ans)
