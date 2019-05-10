from random import sample, randint
from typing import List
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # 邪道すぎたのでswapするやり方書く
        # return sample(self.nums, len(self.nums))
        for i in range(len(self.nums)):
            idx = randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
nums = [1,2,3,4,5]
obj = Solution(nums)
param_0 = obj.shuffle()
param_1 = obj.reset()
param_2 = obj.shuffle()

print(param_0)
print(param_1)
print(param_2)
