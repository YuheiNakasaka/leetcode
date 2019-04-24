from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
          pass

        tmpDict = {}
        for i in range(len(nums)):
            tmpDict[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in tmpDict and tmpDict[complement] != i:
              return [i, tmpDict[complement]]


solution = Solution()
print(solution.twoSum([0,4,3,0], 0))
print(solution.twoSum([1,2,4], 3))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum(range(0, 5000000), 4199999))
