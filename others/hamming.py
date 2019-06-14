class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

solution = Solution()
print(solution.hammingWeight(0b00000000000000000000000000001011))