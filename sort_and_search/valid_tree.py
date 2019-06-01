# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        if root.left == None and root.right == None:
            return True
        else:
            if root.right == None and root.left and root.left.val < root.val:
                return self.isValidBST(root.left)
            elif root.left == None and root.right and root.right.val > root.val:
                return self.isValidBST(root.right)
            elif root.right and root.left and root.left.val < root.val < root.right.val:
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False

tree = TreeNode(2)
tree1 = TreeNode(1)
tree1.left = TreeNode(0)
tree1.right = TreeNode(2)
tree2 = TreeNode(3)
tree2.left = TreeNode(2)
tree2.right = TreeNode(5)
tree.left = tree1
tree.right = tree2
solution = Solution()
print("Success") if solution.isValidBST(tree) else print("Fail")

tree = TreeNode(1)
tree.right = TreeNode(2)
solution = Solution()
print("Success") if solution.isValidBST(tree) else print("Fail")

tree = TreeNode(1)
tree.right = TreeNode(0)
solution = Solution()
print("Success") if solution.isValidBST(tree) == False else print("Fail")