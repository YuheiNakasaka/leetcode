X = int(input())

def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

pn = primes(10**6)

def bsearch(v, l, r):
    if l >= r - 1:
        return [l, r]
    m = l + ((r - l) // 2)
    if pn[m] < v:
        return bsearch(v, m, r)
    else:
        return bsearch(v, l, m)

l, r = bsearch(X, 0, len(pn))
# print(l, r)
# print(pn[l], pn[r])
if X == 2:
    print(2)
else:
    print(pn[r])
