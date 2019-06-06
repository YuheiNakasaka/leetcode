class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # time limit exceeded
        # result = 0
        # for i in range(len(prices)):
        #     for k in prices[i:]:
        #         profit = k - prices[i]
        #         if result < profit:
        #             result = profit
        # return result
        min_price = 2**31-1
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > profit:
                profit = prices[i] - min_price
        return profit

solution = Solution()
resp = solution.maxProfit([7,1,5,3,6,4])
print('Success ', resp) if resp == 5 else print('Fail ', resp)

resp = solution.maxProfit([7,6,4,3,1])
print('Success ', resp) if resp == 0 else print('Fail ', resp)

[4,2,5,6,1,3]

resp = solution.maxProfit(list(range(0, 10000000)))
print('Success ', resp) if resp == 0 else print('Fail ', resp)