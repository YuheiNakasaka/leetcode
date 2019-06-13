# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         result = 0
#         first_limit = 0
#         last_limit = len(nums) - 1
#         for i in range(len(nums)):
#             outcome = 0
#             curr = i
#             left_side = i - 2
#             right_side = i + 2
#             if left_side >= first_limit:
#                 outcome += nums[left_side]
#             if right_side <= last_limit:
#                 outcome += nums[right_side]
#             outcome += nums[curr]
#             if result < outcome: result = outcome
#         return result

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
        for cur in num:
            max_3_house_before, max_2_house_before, adjacent = \
            max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)
        return max(max_2_house_before, adjacent)

solution = Solution()
resp = solution.rob([1,2,3,1])
print(resp)
resp = solution.rob([2,7,9,3,1])
print(resp)