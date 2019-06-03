# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 上から順にnode.valを積んでいって、left/rightの全てのnodeをlevel配列にし、次のループへみたいな感じ
    # でlevelがなくなるまで続ける
    def levelOrder(self, root):
      ans, level = [], [root]
      while root and level:
          ans.append([node.val for node in level])
          LRpair = [(node.left, node.right) for node in level]
          level = [leaf for LR in LRpair for leaf in LR if leaf]
      return ans

    # # Easy solution to understand
    # def levelOrder(self, root):
    #     ret = []
    #     level = [root]
    #     while root and level:
    #         currentNodes = []
    #         nextLevel = []
    #         for node in level:
    #             currentNodes.append(node.val)
    #             if node.left:
    #                 nextLevel.append(node.left)
    #             if node.right:
    #                 nextLevel.append(node.right)
    #         ret.append(currentNodes)
    #         level = nextLevel
    #     return ret

tree = TreeNode(3)
treel1 = TreeNode(9)
treer1 = TreeNode(20)
treer1.left = TreeNode(15)
treer1.right = TreeNode(7)