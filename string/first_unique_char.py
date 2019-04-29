from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = list(s)
        h = {}
        for i in range(len(arr)):
            h[arr[i]] = h.get(arr[i], 0) + 1
        
        for i in range(len(arr)):
            if h[arr[i]] == 1:
                return i
        return -1

# なぜかこっちの方が速いけど汚い
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         arr = list(s)
#         h = {}
#         n = len(arr)
#         for i in range(len(arr)):
#             if arr[i] not in h:
#                 h[arr[i]] = i
#             else:
#                 h[arr[i]] = n

#         idx = n
#         for k, i in h.items():
#             if i == n: continue
#             if idx > i:
#                 idx = i

#         if idx == n: return -1
#         else: return idx

solution = Solution()

# 1
arr = "leetcode"
resp = solution.firstUniqChar(arr)
if resp == 0:
    print('Success')
print(resp)

# 2
arr = "loveleetcode"
resp = solution.firstUniqChar(arr)
if resp == 2:
    print('Success')
print(resp)

# 3
arr = "aaaaaaa"
resp = solution.firstUniqChar(arr)
if resp == -1:
    print('Success')
print(resp)
