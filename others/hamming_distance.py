# ハミング距離は2進数表現のx,yを比べた時に各桁で異なる数の個数のこと
# 例えば
# 101
# 001
# の場合はハミング距離は2となる
# class Solution(object):
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         res = 0
#         bx = format(x, 'b').zfill(32)
#         by = format(y, 'b').zfill(32)
#         for i in range(len(bx)):
#           if bx[i] is not by[i]:
#               res += 1
#         return res

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return format(x^y, 'b').count('1')
        

solution = Solution()
print("Success") if solution.hammingDistance(1, 4) == 2 else print('Fail')