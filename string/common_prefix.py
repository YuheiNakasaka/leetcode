from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        m = "" 
        first = strs[0]
        for i in range(len(first)):
            check = 0
            n = len(strs[1:])
            for s in strs[1:]:
                if i < len(s) and s[i] == first[i]:
                    check += 1
                else:
                    return m
            if check == n:
                check = 0
                m += first[i]
        return m





solution = Solution()
a = ["flower","flow","flight"]
resp = solution.longestCommonPrefix(a)
if resp == "fl":
    print("Success")

a = ["dog","racecar","car"]
resp = solution.longestCommonPrefix(a)
if resp == "":
    print("Success")

a = ["dog", ""]
resp = solution.longestCommonPrefix(a)
if resp == "":
    print("Success")

a = ["aca","cba"]
resp = solution.longestCommonPrefix(a)
if resp == "":
    print("Success")