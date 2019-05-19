from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a, i, j = [], 0, 0
        while j < n and m > 0 and n > 0:
            if nums1[i] == nums2[j]:
                a.append(nums2[j])
                a.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                a.append(nums2[j])
                j += 1
            else:
                a.append(nums1[i])
                i += 1
            if i == m: break
        if i < m:
            a[m+n-len(nums1[i:m]):] = nums1[i:m]
        if j < n:
            a[m+n-len(nums2[j:]):] = nums2[j:]
        nums1[:] = a

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
        
#         k = m + n - 1
#         i = m - 1
#         j = n - 1
#         while k >= 0:
#             if i >= 0 and j >= 0:
#                 if nums1[i] >= nums2[j]:
#                     nums1[k] = nums1[i]
#                     i -= 1
#                 else:
#                     nums1[k] = nums2[j]
#                     j -= 1
#             elif j >= 0:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             else:
#                 break
#             k -= 1

solution = Solution()

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
solution.merge(nums1, 3, nums2, 3)
print("Success") if nums1 == [1,2,2,3,5,6] else print("Fail")

nums1 = [1,2,3,0,0,0]
nums2 = [5,6,7]
solution.merge(nums1, 3, nums2, 3)
print("Success") if nums1 == [1,2,3,5,6,7] else print("Fail")

nums1 = [5,6,7,0,0,0]
nums2 = [1,2,3]
solution.merge(nums1, 3, nums2, 3)
print("Success") if nums1 == [1,2,3,5,6,7] else print("Fail")

nums1 = [1,2,7,0,0,0]
nums2 = [2,5,6]
solution.merge(nums1, 3, nums2, 3)
print("Success") if nums1 == [1,2,2,5,6,7] else print("Fail")

nums1 = [0,0,0,0]
nums2 = [2,5,6]
solution.merge(nums1, 1, nums2, 3)
print("Success") if nums1 == [0,2,5,6] else print("Fail")

nums1 = [1,2,4,5,6,0]
nums2 = [3]
solution.merge(nums1, 5, nums2, 1)
print("Success") if nums1 == [1,2,3,4,5,6] else print("Fail")