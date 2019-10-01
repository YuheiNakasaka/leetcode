import sys
readline = sys.stdin.readline
A,B = list(map(int, readline().split()))

# def get_sieve_of_eratosthenes(n):
#     if not isinstance(n, int):
#         raise TypeError("n is int-type.")
#     if n < 2:
#         raise ValueError("n is more than 2")
#     data = [i for i in range(2, n + 1)]
#     for d in data:
#         data = [x for x in data if (x == d or x % d != 0)]
#     return data

def factorization(n):
    arr = [[1,1]]
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def gdc(x,y):
    if y == 0:
        return x
    return gdc(y, x % y)

g = gdc(B,A)
res = factorization(g)
# print(g,res)
print(len(res))
