class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1: return True
        while True:
            i = n % 3
            if i > 0: return False
            n = n / 3
            if n == 1:
              return True

# こんなんチートやん...
# IntのMaxが3**19なのでその範囲にしかnが存在し得ないことを利用する
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         return n > 0 and 1162261467 % n == 0

solution = Solution()
print("Success") if solution.isPowerOfThree(27) else print("Fail")
print("Success") if solution.isPowerOfThree(9) else print("Fail")
print("Success") if solution.isPowerOfThree(243) else print("Fail")
print("Success") if solution.isPowerOfThree(1) else print("Fail")
print("Success") if solution.isPowerOfThree(0) == False else print("Fail")
print("Success") if solution.isPowerOfThree(-3) == False else print("Fail")
print("Success") if solution.isPowerOfThree(45) == False else print("Fail")