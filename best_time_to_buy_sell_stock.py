from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit

solution = Solution()

result = solution.maxProfit([7,1,5,3,6,4])
if result == 7:
    print('Success')
print(result)

result = solution.maxProfit([1,2,3,4,5])
if result == 4:
    print('Success')
print(result)

result = solution.maxProfit([7,6,4,3,1])
if result == 0:
    print('Success')
print(result)

result = solution.maxProfit(range(0, 5000000))
if result == 4999999:
    print('Success')
print(result)
