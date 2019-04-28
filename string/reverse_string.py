from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1

solution = Solution()

# 1
arr = ["h","e","l","l","o"]
solution.reverseString(arr)
if arr == ["o","l","l","e","h"]:
    print('Success')
print(arr)
# 2
arr = ["H","a","n","n","a","h"]
solution.reverseString(arr)
if arr == ["h","a","n","n","a","H"]:
    print('Success')
print(arr)