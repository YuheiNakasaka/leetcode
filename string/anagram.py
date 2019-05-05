class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = "".join(sorted(s))
        ts = "".join(sorted(t))
        if ss == ts:
            return True
        return False

solution = Solution()

if solution.isAnagram("anagram", "nagaram") == True:
    print("Success")

if solution.isAnagram("rat", "cat") == False:
    print("Success")

if solution.isAnagram("", "") == True:
    print("Success")

if solution.isAnagram("hello", "ello") == False:
    print("Success")