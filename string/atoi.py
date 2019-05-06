import re
# 正規表現でゴリゴリやっていく方法
class Solution:
    def myAtoi(self, str: str) -> int:  
        str = re.sub(r'^\s+', '', str)
        if re.match(r'^[^\s|\d|\-|\+]', str): return 0
        if re.match(r'^\+[^\d]', str): return 0
        if re.match(r'^\-[^\d]', str): return 0
        str = re.sub(r'^\+', '', str)
        result = re.match(r'^-{0,1}\d+', str)
        if result:
            num = int(result[0])
            if -(2**31) >= num: return -2147483648
            if 2**31 <= num: return 2147483647
            return num
        return 0

# 1) head,tailの空白を取り去る
# 2) 符号をチェック
# 3) それ以降の値が全て数値かどうかチェック
# 4) 極値をチェック
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         str = str.strip()
#         if str == "": return 0
#         ss = ""
#         pos_neg = 1
#         if str[0] == "-":
#             pos_neg = -1
#             str = str[1:]
#         elif str[0] == "+":
#             str = str[1:]
#         for s in str:
#             if s in "0123456789":
#                 ss += s
#             else:
#                 break
#         if ss == "": return 0
#         result = int(ss)*pos_neg
#         max, min = (2 ** 31) - 1 , -2 ** 31
#         if result > max:
#             return max
#         elif result < min:
#             return min
#         return result

solution = Solution()

# 1
result = solution.myAtoi("42")
print("Success") if result == 42 else print("Fail")
print(result)

# 2
result = solution.myAtoi("   -42 ")
print("Success") if result == -42 else print("Fail")
print(result)

# 3
result = solution.myAtoi("4193 with words")
print("Success") if result == 4193 else print("Fail")
print(result)

# 4
result = solution.myAtoi("words and 987")
print("Success") if result == 0 else print("Fail")
print(result)

# 5
result = solution.myAtoi("-91283472332")
print("Success") if result == -2147483648 else print("Fail")
print(result)

# 6
result = solution.myAtoi("     ")
print("Success") if result == 0 else print("Fail")
print(result)

# 7
result = solution.myAtoi("-  was")
print("Success") if result == 0 else print("Fail")
print(result)

# 8
result = solution.myAtoi("0-1")
print("Success") if result == 0 else print("Fail")
print(result)

# 9
result = solution.myAtoi("--2")
print("Success") if result == 0 else print("Fail")
print(result)

# 10
result = solution.myAtoi("+2")
print("Success") if result == 2 else print("Fail")
print(result)

# 11
result = solution.myAtoi("+-2")
print("Success") if result == 0 else print("Fail")
print(result)

# 12
result = solution.myAtoi("-+2")
print("Success") if result == 0 else print("Fail")
print(result)

# 13
result = solution.myAtoi("  +-1 +0 123")
print("Success") if result == 0 else print("Fail")
print(result)

# 14
result = solution.myAtoi("2147483648")
print("Success") if result == 2147483647 else print("Fail")
print(result)

# 15
result = solution.myAtoi("-91283472332")
print("Success") if result == -2147483648 else print("Fail")
print(result)