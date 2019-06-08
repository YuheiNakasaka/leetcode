from typing import List

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maximum = -(2**31-1)
#         minimum = 2**31-1
#         max_i = 0
#         mini_i = 0
#         diff = -(2**31-1)
#         for i in range(len(nums)):
#             if maximum < nums[i]:
#                 maximum = nums[i]
#                 max_i = i
#             if minimum > nums[i]:
#                 minimum = nums[i]
#                 mini_i = i
#             if max_i > mini_i:
#                 if sum(nums[mini_i:max_i+1]) > diff:
#                     diff = sum(nums[mini_i:max_i])
#             else:
#                 if sum(nums[max_i:mini_i+1]) > diff:
#                     diff = sum(nums[max_i:mini_i])
#         return diff

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

solution = Solution()
resp = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print("Success ", resp) if resp == 6 else print("Fail ", resp)
resp = solution.maxSubArray([-2,1,4])
print("Success ", resp) if resp == 5 else print("Fail ", resp)