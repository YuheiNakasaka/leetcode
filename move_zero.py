from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = cnt = 0
        while cnt < len(nums):
            if nums[i] == 0: nums.append(nums.pop(i))
            else: i += 1
            cnt += 1


solution = Solution()
arr = [0,1,0,3,12]
solution.moveZeroes(arr)
if arr == [1,3,12,0,0]:
    print('Success')
print(arr)
