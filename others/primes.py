n = 100
primes = {i for i in range(2, n + 1)}
for i in range(2, int(n**0.5 + 1)):
    primes.difference_update(list(range(i*2, n + 1, i)))
print(primes)