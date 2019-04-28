from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            pass
        else:
            head = nums[len(nums) - k : len(nums)]
            tail = nums[0 : len(nums) - k]
            nums[:] = head + tail

# Sample
# Time: O(n), Memory: O(n)
nums = [1,2,3,4,5,6,7]
solution = Solution()
solution.rotate(nums, 3)
if nums == [5,6,7,1,2,3,4]:
    print('Accepted')
else:
    print('Failed')
