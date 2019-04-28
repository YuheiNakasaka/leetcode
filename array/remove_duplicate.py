from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash = {}
        for i, num in enumerate(nums):
            hash[num] = 0
        nums.clear()
        nums.extend(hash.keys())
        return len(nums)

solution = Solution()
arr = [1,1,2,3,4,4,5]
print(solution.removeDuplicates(arr))
print(arr)
