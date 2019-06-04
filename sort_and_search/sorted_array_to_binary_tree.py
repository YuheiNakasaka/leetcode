# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root

solution = Solution()
trees = solution.sortedArrayToBST([-10,-3,0,5,9])

def traverse(tree):
    if not tree: return
    print(tree.val)
    if tree.left: traverse(tree.left)
    if tree.right: traverse(tree.right)

traverse(trees)

print("")

# [3,1,5,0,2,4]
trees = solution.sortedArrayToBST([0,1,2,3,4,5])
traverse(trees)