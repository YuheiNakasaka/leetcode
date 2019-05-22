# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

solution = Solution()
listNode = ListNode(4)
listNode.next = ListNode(5)
listNode.next.next = ListNode(1)
listNode.next.next.next = ListNode(9)
solution.deleteNode(listNode)