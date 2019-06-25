class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        resList = []
        currList = [1]
        for i in range(1, numRows + 1):
            currList = self.nextList(currList, i)
            resList.append(currList)
        return resList

    def nextList(self, prevList, numRows):
        if numRows == 1: return prevList
        nextList = []
        n = 0
        while n < numRows:
            if n - 1 < 0 or n >= len(prevList): 
                nextList.append(prevList[n - 1])
            else:
                nextList.append(prevList[n - 1] + prevList[n])
            n += 1
        return nextList
        


solution = Solution()
print(solution.generate(20))