# 遅くて終わらんやつ
# import math
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         count = 0
#         i = n - 1
#         while 1 < i:
#             if self.isPrime(i):
#                 count += 1
#             i = i - 1
#         return count 

#     def isPrime(self, n: int) -> bool:
#         if n == 1: return False
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 return False
#         return True

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        prime = [1] * n
        for i in range(2,int(n*0.5)+1):
            prime[i*i:n:i] = [0] * len(prime[i*i:n:i])
        return sum(prime)-2

solution = Solution()
print("Success") if solution.countPrimes(10) == 4 else print("Fail")
print("Success") if solution.countPrimes(2) == 0 else print("Fail")
print("Success") if solution.countPrimes(1) == 0 else print("Fail")
print("Success") if solution.countPrimes(0) == 0 else print("Fail")
print("Success") if solution.countPrimes(100) == 25 else print("Fail")
print("Success") if solution.countPrimes(11) == 4 else print("Fail")
print("Success") if solution.countPrimes(499979) == 41537 else print("Fail")
print("Success") if solution.countPrimes(999983) == 78497 else print("Fail")
