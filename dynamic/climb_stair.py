class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * n
        return self.memo_fib(n, memo)

    def memo_fib(self, n, memo):
        if n == 0: return 1
        if n == 1: return 1
        if memo[n - 1] > 0: return memo[n - 1]
        memo[n - 1] = self.memo_fib(n-1, memo) + self.memo_fib(n-2, memo)
        return memo[n - 1]


solution = Solution()

resp = solution.climbStairs(2)
print('Success: ', resp) if resp == 2 else print('Fail: ', resp)
resp = solution.climbStairs(3)
print('Success: ', resp) if resp == 3 else print('Fail: ', resp)
resp = solution.climbStairs(4)
print('Success: ', resp) if resp == 5 else print('Fail: ', resp)
resp = solution.climbStairs(5)
print('Success: ', resp) if resp == 8 else print('Fail: ', resp)

resp = solution.climbStairs(38)
print(resp)