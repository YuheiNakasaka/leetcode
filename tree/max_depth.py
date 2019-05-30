# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root, 1)
    
    def traverse(self, tree, n):
        if tree == None: return 0
        if tree.left == None and tree.right == None:
            return n
        elif tree.left == None and tree.right:
            return self.traverse(tree.right, n + 1)
        elif tree.left and tree.right == None:
            return self.traverse(tree.left, n + 1)
        else:
            l = self.traverse(tree.left, n + 1)
            r = self.traverse(tree.right, n + 1)
            return r if r > l else l

# 別解。解けば良いのか〜〜
# class Solution:
#     # @param {TreeNode} root
#     # @return {integer}
#     def maxDepth(self, root):
#         if not root:
#             return 0

#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

tree = TreeNode(3)
tree.left = TreeNode(9)
tree2 = TreeNode(20)
tree2.left = TreeNode(15)
tree2.right = TreeNode(7)
tree.right = tree2

solution = Solution()
print("Success") if solution.maxDepth(tree) == 3 else print("Fail")