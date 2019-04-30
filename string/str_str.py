class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "": return 0

        idx = 0
        n = len(needle)
        while idx < len(haystack):
            if haystack[idx:idx+n] == needle:
                return idx
            idx += 1
        return -1

solution = Solution()

# 1
haystack = "igllav"
needle  = "la"
resp = solution.strStr(haystack, needle)
if resp == 3:
    print('Success')

# 2
haystack = "aaaaaa"
needle  = "bbb"
resp = solution.strStr(haystack, needle)
if resp == -1:
    print('Success')

# 3
haystack = "aaaaaa"
needle  = "aa"
resp = solution.strStr(haystack, needle)
if resp == 0:
    print('Success')

# 4
haystack = ""
needle  = ""
resp = solution.strStr(haystack, needle)
if resp == 0:
    print('Success')

# 5
haystack = "akbvuadv"
needle  = "dv"
resp = solution.strStr(haystack, needle)
if resp == 6:
    print('Success')
