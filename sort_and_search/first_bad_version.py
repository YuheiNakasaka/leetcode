# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# In case first bad version is 4
def isBadVersion(version: int) -> bool:
    return 6 <= version

# Memory Error
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         l = list(range(1, n + 1))
#         while True:
#             p = int(len(l) / 2)
#             if isBadVersion(l[p]) == True:
#                 l = l[:p + 1]
#                 if len(l) == 2: break
#             else:
#                 l = l[p:]
#             if len(l) <= 2: break
#         return l[-1]

# Binary Search
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r  = 1, n
        while r >= l:
            mid = (l + r)//2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

solution = Solution()
print("Success") if solution.firstBadVersion(2**24) == 6 else print("Fail")
print("Success") if solution.firstBadVersion(6) == 6 else print("Fail")