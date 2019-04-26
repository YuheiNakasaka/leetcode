from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        h = {}
        for num in nums1:
            h[num] = h.get(num, 0) + 1
        
        for num in nums2:
            try:
                if h[num] > 0:
                    result.append(num)
                    h[num] -= 1
            except KeyError:
                pass
        return result


solution = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
result = solution.intersect(nums1, nums2)
if result == [2,2]:
    print('Success')
print(result)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result = solution.intersect(nums1, nums2)
if result == [4,9]:
    print('Success')
print(result)