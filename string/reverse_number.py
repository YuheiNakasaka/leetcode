class Solution:
    def reverse(self, x: int) -> int:
        chars = [s for s in str(x)]
        result = 0
        if chars[0] == "-":
          result = int("-" + "".join(chars[1:len(chars)][::-1]))
        else:
          result = int("".join(chars[::-1]))
        
        if -(2**31) > result: return 0
        if 2**31 < result: return 0
        return result

solution = Solution()

# 1
input = 123
result = solution.reverse(input)
if result == 321:
    print('Success')
print(result)

# 2
input = -123
result = solution.reverse(input)
if result == -321:
    print('Success')
print(result)

# 1
input = 120
result = solution.reverse(input)
if result == 21:
    print('Success')
print(result)