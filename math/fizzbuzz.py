from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        i = 1
        while i <= n:
            if  i % 15 == 0:
                l.append("FizzBuzz")
            elif i % 3 == 0:
                l.append("Fizz")
            elif i % 5 == 0:
                l.append("Buzz")
            else:
                l.append(str(i))
            i += 1
        return l

solution = Solution()
print(solution.fizzBuzz(15))