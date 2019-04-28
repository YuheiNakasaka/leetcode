from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_duplication(hash):
          for value in hash.values():
              if value > 1:
                  return False

        # Check rows
        i = j = 0
        h = {}
        while i < 9:
          if board[i][j] != '.': h[board[i][j]] = h.get(board[i][j], 0) + 1
          j += 1
          if j == 9:
            if check_duplication(h) == False: return False
            h = {}
            j = 0
            i += 1

        # Check columns
        i = j = 0
        h = {}
        while i < 9:
          if board[j][i] != '.': h[board[j][i]] = h.get(board[j][i], 0) + 1
          j += 1
          if j == 9:
            if check_duplication(h) == False: return False
            h = {}
            j = 0
            i += 1

        # Check 3 x 3 
        i = j = cnt = 0
        while cnt < 9:
          h = {}
          if board[3 * i][3 * j] != '.': h[board[3 * i][3 * j]] = h.get(board[3 * i][3 * j], 0) + 1
          if board[3 * i][3 * j + 1] != '.': h[board[3 * i][3 * j + 1]] = h.get(board[3 * i][3 * j + 1], 0) + 1
          if board[3 * i][3 * j + 2] != '.': h[board[3 * i][3 * j + 2]] = h.get(board[3 * i][3 * j + 2], 0) + 1
          if board[3 * i + 1][3 * j] != '.': h[board[3 * i + 1][3 * j]] = h.get(board[3 * i + 1][3 * j], 0) + 1
          if board[3 * i + 1][3 * j + 1] != '.': h[board[3 * i + 1][3 * j + 1]] = h.get(board[3 * i + 1][3 * j + 1], 0) + 1
          if board[3 * i + 1][3 * j + 2] != '.': h[board[3 * i + 1][3 * j + 2]] = h.get(board[3 * i + 1][3 * j + 2], 0) + 1
          if board[3 * i + 2][3 * j] != '.': h[board[3 * i + 2][3 * j]] = h.get(board[3 * i + 2][3 * j], 0) + 1
          if board[3 * i + 2][3 * j + 1] != '.': h[board[3 * i + 2][3 * j + 1]] = h.get(board[3 * i + 2][3 * j + 1], 0) + 1
          if board[3 * i + 2][3 * j + 2] != '.': h[board[3 * i + 2][3 * j + 2]] = h.get(board[3 * i + 2][3 * j + 2], 0) + 1

          if check_duplication(h) == False: return False

          j += 1
          if j == 3:
              j = 0
              i += 1
          cnt += 1
        
        return True

solution = Solution()
arr = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
result = solution.isValidSudoku(arr)
if result == True:
    print('Success')
else:
    print('Failed')