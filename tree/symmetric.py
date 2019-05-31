# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 解けなかった..
# 再帰構造捉えるの下手すぎる
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if not root: return True
#         pass

class Solution:
  def isSymmetric(self, root):
    if root is None:
      return True
    else:
      return self.isMirror(root.left, root.right)

  def isMirror(self, left, right):
    if left is None and right is None:
      return True
    if left is None or right is None:
      return False

    if left.val == right.val:
      outPair = self.isMirror(left.left, right.right)
      inPiar = self.isMirror(left.right, right.left)
      return outPair and inPiar
    else:
      return False


tree = TreeNode(1)
tree_left = TreeNode(2)
tree_left.left = TreeNode(3)
tree_left.right = TreeNode(4)
tree_right = TreeNode(2)
tree_right.left = TreeNode(4)
tree_right.right = TreeNode(3)
tree.left = tree_left
tree.right = tree_right

solution = Solution()
print("Success") if solution.isSymmetric(tree) == True else print("Fail")