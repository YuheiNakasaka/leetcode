class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(list(range(0, len(nums) + 1)))
        m = sum(nums)
        return s - m
 
s = Solution()
print("Success") if s.missingNumber([3,0,1]) == 2 else print("Fail")
print("Success") if s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8 else print("Fail")