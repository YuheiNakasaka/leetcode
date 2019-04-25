from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        coln = len(matrix[0]) - 1
        arr = [[0 for col in range(n)] for row in range(n)]
        for i in range(n):
            col = coln - i
            for j in range(len(matrix[i])):
                row = j
                arr[row][col] = matrix[i][j]
        matrix[:] = arr

class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = zip(*matrix[::-1])

# 自力解法
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
solution = Solution()
print(matrix)
solution.rotate(matrix)
print(matrix)

# 模範解法
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
solution = Solution2()
print(matrix)
solution.rotate(matrix)
print(matrix)