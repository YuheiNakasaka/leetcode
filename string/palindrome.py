import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^\w]', '', s)
        ss = [char.lower() for char in s]
        return ss == ss[::-1]

# 最初に実装したクソ遅い例
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         chars = list(s)
#         chars = [char.lower() for char in chars if re.match('\w', char)]
#         i = 0
#         j = len(chars) - 1
#         while i < j:
#             if chars[i] != chars[j]:
#                 return False
#             i += 1
#             j -= 1
#         return  True


solution = Solution()

# 1
s = "A man, a plan, a canal: Panama"
resp = solution.isPalindrome(s)
if resp == True:
    print('Success')

# 2
s = "race a car"
resp = solution.isPalindrome(s)
if resp == False:
    print('Success')

# 3
s = "0P"
resp = solution.isPalindrome(s)
if resp == False:
    print('Success')